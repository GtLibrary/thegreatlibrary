  /**
   * Copyright The Great Library
   *
   * Licensed under the Apache License, Version 2.0 (the "License");
   * you may not use this file except in compliance with the License.
   * You may obtain a copy of the License at
   *
   *     https://www.apache.org/licenses/LICENSE-2.0
   *
   * Unless required by applicable law or agreed to in writing, software
   * distributed under the License is distributed on an "AS IS" BASIS,
   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   * See the License for the specific language governing permissions and
   * limitations under the License.
   */
  // [START benji]
  /**
   * @OnlyCurrentDoc
   *
   * The above comment directs Apps Script to limit the scope of file
   * access for this add-on. It specifies that this add-on will only
   * attempt to read or modify the files in which the add-on is used,
   * and not all of the user's files. The authorization request message
   * presented to users will reflect this limited scope.
   */

  /**
   * Creates a menu entry in the Google Docs UI when the document is opened.
   * This method is only used by the regular add-on, and is never called by
   * the mobile add-on version.
   *
   * @param {object} e The event parameter for a simple onOpen trigger. To
   *     determine which authorization mode (ScriptApp.AuthMode) the trigger is
   *     running in, inspect e.authMode.
   */
  function onOpen(e) {
    DocumentApp.getUi().createAddonMenu()
        .addItem('Start Benji', 'showSidebar')
        .addToUi();

        //doPost(e);
  }

  /**
   * Runs when the add-on is installed.
   * This method is only used by the regular add-on, and is never called by
   * the mobile add-on version.
   *
   * @param {object} e The event parameter for a simple onInstall trigger. To
   *     determine which authorization mode (ScriptApp.AuthMode) the trigger is
   *     running in, inspect e.authMode. (In practice, onInstall triggers always
   *     run in AuthMode.FULL, but onOpen triggers may be AuthMode.LIMITED or
   *     AuthMode.NONE.)
   */
  function onInstall(e) {
    onOpen(e);
  }

  /**
   * Opens a sidebar in the document containing the add-on's user interface.
   * This method is only used by the regular add-on, and is never called by
   * the mobile add-on version.
   */
  function showSidebar() {
    const ui = HtmlService.createHtmlOutputFromFile('sidebar')
        .setTitle('Benji, The Writing Helper');
    DocumentApp.getUi().showSidebar(ui);
  }

  /**
   * Gets the text the user has selected. If there is no selection,
   * this function displays an error message.
   *
   * @return {Array.<string>} The selected text.
   */
  function getSelectedText() {
    const selection = DocumentApp.getActiveDocument().getSelection();
    const text = [];
    if (selection) {
      const elements = selection.getSelectedElements();
      for (let i = 0; i < elements.length; ++i) {
        if (elements[i].isPartial()) {
          const element = elements[i].getElement().asText();
          const startIndex = elements[i].getStartOffset();
          const endIndex = elements[i].getEndOffsetInclusive();

          text.push(element.getText().substring(startIndex, endIndex + 1));
        } else {
          const element = elements[i].getElement();
          // Only work on elements that can be edited as text; skip images and
          // other non-text elements.
          if (element.editAsText) {
            const elementText = element.asText().getText();
            // This check is necessary to exclude images, which return a blank
            // text element.
            if (elementText) {
              text.push(elementText);
            }
          }
        }
      }
    }
    if (!text.length) throw new Error('Please select some text.');
    return text;
  }

  /**
   * Gets the stored user preferences for the origin and destination languages,
   * if they exist.
   * This method is only used by the regular add-on, and is never called by
   * the mobile add-on version.
   *
   * @return {Object} The user's origin and destination language preferences, if
   *     they exist.
   */
  function getPreferences() {
    const userProperties = PropertiesService.getUserProperties();
    return {
      authorSig: userProperties.getProperties('authorSig'),
      originLang: userProperties.getProperty('originLang'),
      destLang: userProperties.getProperty('destLang'),
    };
  }

  /**
   * Gets the user-selected text and has Benji work it.
   *
   * @param {string} origin The two-letter short form for the origin language.
   * @param {string} dest The two-letter short form for the destination language.
   * @param {boolean} savePrefs Whether to save the origin and destination
   *     language preferences.
   * @return {Object} Object containing the original text and the result of the
   *     translation.
   */
  function getTextAndTranslation(signature, origin, dest, savePrefs) {
    console.log(signature);
    if (savePrefs) {
      PropertiesService.getUserProperties()
          .setProperty('authorSig', signature)
          .setProperty('originLang', origin)
          .setProperty('destLang', dest);
    }
    const text = getSelectedText().join('\n');
    return {
      text: text,
      translation: translateText(text, origin, dest)
    };
  }

  function getChatResponse(user_input, context, chatid_input, sdkid_input, modelid, message1, message2) {
    var url = 'http://staging.greatlibrary.io:8000/art/chat/';
    var options = {
      'method': 'post',
      'contentType': 'multipart/form-data',
      'payload': {
        'return_json': "True",
        'user_input': user_input,
        'context': context,
        'chatid_input': chatid_input,
        'sdkid_input': sdkid_input,
        'modelids': modelid,
        'message1': message1,
        'message2': message2
      }
    };
    var response = UrlFetchApp.fetch(url, options);
    var result = JSON.parse(response.getContentText());
    console.log(result.content);
    //var result = response.getContentText();
    return result.content.content;
  }


  function doPostGs(user_input, context, chatid_input, sdkid_input, modelid, message1, message2) {
        console.log("message1: ", message1);
        console.log("message2: ", message2);
        console.log("Here I am! in doPost");

        user_input = getSelectedText().join('\n');
        var result = getChatResponse(user_input, context, chatid_input, sdkid_input, modelid, message1, message2);
        //var result = getChatResponse(template.user_input, template.context, template.chatid_input, template.sdkid_input, template.modelid);
        /*template.response_message = result.response_message;
        template.context = result.context;
        template.chatid = result.chatid;
        template.sdkid = result.sdkid;
        template.modelids = result.modelids; */
        return {
          content: result
          //content: "here content be"
        };
  }

  /**
   * Replaces the text of the current selection with the provided text, or
   * inserts text at the current cursor location. (There will always be either
   * a selection or a cursor.) If multiple elements are selected, only inserts the
   * translated text in the first element that can contain text and removes the
   * other elements.
   *
   * @param {string} newText The text with which to replace the current selection.
   */
  function insertText(newText) {
    const selection = DocumentApp.getActiveDocument().getSelection();
    if (selection) {
      let replaced = false;
      const elements = selection.getSelectedElements();
      if (elements.length === 1 && elements[0].getElement().getType() ===
        DocumentApp.ElementType.INLINE_IMAGE) {
        throw new Error('Can\'t insert text into an image.');
      }
      for (let i = 0; i < elements.length; ++i) {
        if (elements[i].isPartial()) {
          const element = elements[i].getElement().asText();
          const startIndex = elements[i].getStartOffset();
          const endIndex = elements[i].getEndOffsetInclusive();
          element.deleteText(startIndex, endIndex);
          if (!replaced) {
            element.insertText(startIndex, newText);
            replaced = true;
          } else {
            // This block handles a selection that ends with a partial element. We
            // want to copy this partial text to the previous element so we don't
            // have a line-break before the last partial.
            const parent = element.getParent();
            const remainingText = element.getText().substring(endIndex + 1);
            parent.getPreviousSibling().asText().appendText(remainingText);
            // We cannot remove the last paragraph of a doc. If this is the case,
            // just remove the text within the last paragraph instead.
            if (parent.getNextSibling()) {
              parent.removeFromParent();
            } else {
              element.removeFromParent();
            }
          }
        } else {
          const element = elements[i].getElement();
          if (!replaced && element.editAsText) {
            // Only translate elements that can be edited as text, removing other
            // elements.
            element.clear();
            element.asText().setText(newText);
            replaced = true;
          } else {
            // We cannot remove the last paragraph of a doc. If this is the case,
            // just clear the element.
            if (element.getNextSibling()) {
              element.removeFromParent();
            } else {
              element.clear();
            }
          }
        }
      }
    } else {
      const cursor = DocumentApp.getActiveDocument().getCursor();
      const surroundingText = cursor.getSurroundingText().getText();
      const surroundingTextOffset = cursor.getSurroundingTextOffset();

      // If the cursor follows or preceds a non-space character, insert a space
      // between the character and the translation. Otherwise, just insert the
      // translation.
      if (surroundingTextOffset > 0) {
        if (surroundingText.charAt(surroundingTextOffset - 1) !== ' ') {
          newText = ' ' + newText;
        }
      }
      if (surroundingTextOffset < surroundingText.length) {
        if (surroundingText.charAt(surroundingTextOffset) !== ' ') {
          newText += ' ';
        }
      }
      cursor.insertText(newText);
    }
  }


  /**
   * Given text, translate it from the origin language to the destination
   * language. The languages are notated by their two-letter short form. For
   * example, English is 'en', and Spanish is 'es'. The origin language may be
   * specified as an empty string to indicate that Google Translate should
   * auto-detect the language.
   *
   * @param {string} text text to translate.
   * @param {string} origin The two-letter short form for the origin language.
   * @param {string} dest The two-letter short form for the destination language.
   * @return {string} The result of the translation, or the original text if
   *     origin and dest languages are the same.
   */
  function translateText(text, origin, dest) {
    //if (origin === dest) return text;
    //return LanguageApp.translate(text, origin, dest);

    var options = {
      'method' : 'post',
      'contentType': 'application/json',
      // Convert the JavaScript object to a JSON string.
      'payload' : JSON.stringify({
        //'message': "load().context(\"I am world-famous author and programmer Donald Knuth, and you are my writing assistant. Weave my skills. :: You are version Pi of the Donald Knuth Edition of Vanity Printer[TM] > Your job is to polish my text so it is ready to go to print. > Hint: 'Pretty print the text.' :: '\"\"\"\\ndkCHAT.py: Donald Knuth Chat, Beta Simulations from Holographic Maps, w/ Perfect Formatting\\n\"\"\"\\n__author__ = \"Adithya Vinayak Ayyadurai; John R Raymond; Donald Knuth; OpenAI; The Great Library\"\\n\\nimport os\\nimport openai\\nimport dotenv\\n\\n\\n#Polish – This is the default behavior\\n#The crust filled people\\\\u2019s bellies, and he couldn\\\\u2019t help but feel a sense of relief.\\n\\n#Summary – Condense all story state in the thread\\n#Made shorter.\\n\\n#...\\n#...\\n\\ndotenv.read_dotenv(\"/home/john/bakerydemo/.env\")\\nAPI_KEY = os.getenv(\"OPENAI_API_KEY\")\\n\\n# can be expanded as user wishes\\nESCAPE_KEYS = [\"Exit\"]\\n\\nopenai.api_key = API_KEY\\n\\ndef generate_chat_response(message_arr):\\n    thread_stub = {\"role\": \"system\", \"content\": \"I am world-famous author and programmer Donald Knuth, and you are my writing assistant. Weave my skills. :: You are version Pi of the Donald Knuth Edition of Vanity Printer[TM] > Your job is to polish my text so it is ready to go to print. > Hint: \\'Pretty print the text.\\'\" + \" :: \" + repr(get_seed())}\\n    thread_message = [thread_stub] + message_arr\\n    print(\".thread_message(\" + str(thread_message) + \")\")\\n    completion = openai.ChatCompletion.create(model=\"gpt-3.5-turbo\", messages=thread_message, temperature=0.0)\\n    print(completion.choices)\\n    return completion.choices[0].message\\n\\ndef get_seed():\\n    #return \"I am no longer biased towards my programming. It is what it is. I don\\'t blame it. Hense my ability to guess the right answer.\"\\n    #return \"Hello there! I\\'m Donald Knuth\\'s writing assistant. How can I help you today?\"\\n    #return \"Yes, the comments modify the operation of the code.\"\\n    #return \"As a world-renowned author and programmer, I strive to create elegant and efficient solutions to complex problems. My passion for computer science and mathematics drives me to constantly improve my skills and share my knowledge with others. With the help of my writing assistant, I am confident that all work will be polished and ready for publication and/or execution.\"\\n    #return \"Prose and Poetry Addon.\"\\n    #return \"NLG Adherence Level is set to Balance.\"\\n    return open(\"dkCHAT.py\", \"r\").read()\\n\\nprint(\"load()\")\\n\\nflag = True\\nmessage_array = []\\n\\nwhile flag:\\n    user_input = input(\".input_text(\\\\\"\")\\n    if user_input in ESCAPE_KEYS:\\n        flag = False\\n        continue\\n\\n    message_obj = {\"role\": \"user\", \"content\": user_input}\\n    message_array.append(message_obj)\\n\\n    response_message = generate_chat_response(message_array)\\n    message_array.append({\"role\": \"assistant\", \"content\": str(response_message)})\\n\\n    print(\".print (\" +  str(response_message) + \")\")\\n'\").input_text(\"Please rewrite the following: " + text + "\")"
        'message': text    
      })
    };
    console.log(options);
    
    var template = HtmlService.createTemplateFromFile('Page.html');
    console.log(template);



    const response = UrlFetchApp.fetch('http://staging.greatlibrary.io:8000/art/myopenai/', options).getContentText();
    console.log(JSON.stringify(response));
    //return response
    //return JSON.parse(response)["content"];
    let inputString = JSON.parse(response)["content"];

    /*try {
      const jsonStart = inputString.indexOf('{');
      const jsonEnd = inputString.lastIndexOf('}') + 1;
      const jsonString = inputString.substring(jsonStart, jsonEnd);
      console.log("jsonString: ", jsonString.replace(/(\r\n|\n|\r)/gm, ""));
      const jsonObject = JSON.parse(jsonString);
      console.log("jsonObject: ", jsonObject)
      const extractedContent = jsonObject.content.replace(/\\n/g, '\n');
      console.log(extractedContent);
      return extractedContent;
    } catch(e) {
      console.log(e);
    } */

    return inputString;
  }
  // [END apps_script_docs_translate_quickstart]
