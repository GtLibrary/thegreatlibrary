print("""\nfrom django.shortcuts import render\nimport os\nimport openai\nimport dotenv\n\ndotenv.read_dotenv(\"/home/john/bakerydemo/.env\")\nAPI_KEY = os.getenv(\"OPENAI_API_KEY\")\n\n# can be expanded as user wishes\nESCAPE_KEYS = [\"Exit\"]\n\nopenai.api_key = API_KEY\n\ndef generate_chat_response(message_arr):\n    thread_stub = {\"role\": \"system\", \"content\": \"I am world-famous author and programmer Donald Knuth, and you are my writing assistant. Weave my skills. :: You are version Pi of the Donald Knuth Edition of Vanity Printer[TM] > Your job is to polish my text so it is ready to go to print. > Hint: 'Pretty print the text.'\" + \" :: \" + repr(get_seed())}\n    thread_message = [thread_stub] + message_arr\n    completion = openai.ChatCompletion.create(model=\"gpt-3.5-turbo\", messages=thread_message, temperature=0.0)\n    return completion.choices[0].message\n\ndef get_seed():\n    return open(\"dkCHAT.py\", \"r\").read()\n\ndef chat(request):\n    if request.method == 'POST':\n        user_input = request.POST.get('user_input')\n        message_array = request.session.get('message_array', [])\n        if user_input in ESCAPE_KEYS:\n            request.session.flush()\n            return render(request, 'chat.html')\n        message_obj = {\"role\": \"user\", \"content\": user_input}\n        message_array.append(message_obj)\n        response_message = generate_chat_response(message_array)\n        message_array.append({\"role\": \"assistant\", \"content\": str(response_message)})\n        request.session['message_array'] = message_array\n        return render(request, 'chat.html', {'response_message': response_message})\n    else:\n        request.session.flush()\n        return render(request, 'chat.html')\n""")