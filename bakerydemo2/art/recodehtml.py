    import os   #### REPLACE WITH DB CALLSSS!!!!
    import re
    import gzip
    import json
    import shutil
    from os.path import exists
    import urllib
    
    from filelock import Timeout, FileLock
    
    from django.shortcuts import render
    from django.http import HttpResponse
    from django.http import FileResponse
    
    from django.template import Context, Template
    
    from bakerydemo.breads.models import BreadPage
    from django.utils.safestring import SafeString
    
    import bakerydemo.breads.models as books
    from bakerydemo.art.study import Study
    
class Art:
    def serialtest(request):
    
        whatafrank = "asdasd"
        serial = ["moodle"] * 400
    
        serial[0] = "title='serial is 0'"
        serial[1] = "title='serial is 1 now'"
        serial[2] = "title='serial is 2 now'"
    
        for i in range(300):
            serial[i+2] =  "title='serial is " + str(i+2) + " now'"
    
        context = {
            'serial': serial,
            'whatafrank': whatafrank,
        }   
        return render(request, 'art/serialtest.html', context)
    
    
    def get_serials(curserial_num):
    
        serial = []
        for i in range(int(curserial_num)):
            serial.append(' class=ss title=' + str(i) + ' name=serial.' + str(i)  + ' onmouseover=s(this)')
    
        context = {
            'serial': serial,
            'curserial_num': curserial_num,
        }   
        return context
    
    # FIXME: These are a hack, need to make the art/ directory somehow know about the datamines
    # and the network.
    #
    # TODO: Make configuration file for the art directory/app
    def getartdataminedir(datamine):
        return "/home/john/" + datamine + "/" + datamine + ".nft/"
    
    def getnetwork():
        #f = open("/home/john/richtext/network.txt", 'r')
        #network = f.read()
        #f.close()
        #return network
        #return "mumbai"
        return "polygon"   # From https://docs.moralis.io/moralis-server/web3-sdk/intro
    
    
    def getcontractid(datamine):
        try:
            contactfilename = getartdataminedir(datamine) + "contract.txt"
            f = open(contactfilename, 'r')
            contractid = f.read()
            return contractid.strip()
        except:
            return "unknowncontractid";
    
    
    def gethead(datamine):
    
    
        head = """
    
        <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
        <script src="https://unpkg.com/moralis/dist/moralis.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    
        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    
        <style>
            .modal-content iframe{ margin: 0 auto; display: block; }
        </style>
    
        """
    
        return head
    
    def account(datamine):
    
    
    def getbody(datamine):
    
        network = getnetwork()
        account = getaccount(datamine)
        contractid = getcontractid(datamine)
    
        # How to trigger the iframe popup: <span  data-toggle="modal" data-target="#myModal">good old text</span>
    
        body = """
    
    <div class="container">
    <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog modal-lg">
    <div class="modal-content">
    <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal">&times;</button>
    <h4 class="modal-title">Modal Header</h4>
    </div>
    <div class="modal-body">
        <iframe id="videoContainer" width="800" height="685" src="https://opensea.io/" frameborder="0" allowfullscreen></iframe>
     
    </div>
    <div class="modal-footer">
    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
    </div>
    </div>
    </div>
    </div>
    </div>
    
    
        <div id="app-header-btns"></div>
        <section id="content" class="container"></section>
    
        <script src="/static/js/moralisweb3.js"></script>
        <script src="/static/js/books.nft.js"></script>
    
        <script>
        var datamine = '""" + datamine + """';
        var contractid = '""" + contractid + """';
        var network = '""" + network + """';
    
        var serial_num = 0;
        var curid = "sp.0";
    
    
        async function getinfo() {
            const options = { address: contractid, token_id: serial_num, chain: network };
            const tokenIdOwners = await Moralis.Web3API.token.getTokenIdOwners(options);
            console.log(tokenIdOwners);
            console.log(tokenIdOwners.result);
            console.log("Owner: " + tokenIdOwners.result[0].owner_of);
    
            return tokenIdOwners;
        }
    
        async function getprice() {
            const options = { address: contractid, chain: network };
            const tokenIdPrice = await Moralis.Web3API.token.getTokenPrice(options);
            console.log(tokenIdPrice);
            console.log(tokenIdPrice.result);
    
            return tokenIdOwners;
        }
    
    
        async function onclick_async_getowner() {
            const tokenIdOwners = await getinfo();
            console.log(tokenIdOwners);
            console.log(tokenIdOwners.result);
            console.log("Owner: " + tokenIdOwners.result[0].owner_of);
            var owner = tokenIdOwners.result[0].owner_of;
            const tokenid = tokenIdOwners.result[0].token_id;
    
            if (owner == "0x0000000000000000000000000000000000000000") {
                owner = "Not owned";
            }
    
            console.log(curid);
    
            const curef1 =  document.getElementById(curid)
            console.log("A1: " + curef1.id);
            settitle(curef1, tokenid, owner);
        }
    
        async function onclick_async_getprice() {
            const tokenIdOwners = await getprice();
            console.log(tokenIdOwners);
            console.log(tokenIdOwners.result);
            console.log("Owner: " + tokenIdOwners.result[0].owner_of);
            var owner = tokenIdOwners.result[0].owner_of;
            const tokenid = tokenIdOwners.result[0].token_id;
    
            if (owner == "0x0000000000000000000000000000000000000000") {
                owner = "Not owned";
            }
    
            console.log(curid);
    
            const curef1 =  document.getElementById(curid)
            console.log("A1: " + curef1.id);
            settitle(curef1, tokenid, owner);
        }
    
        // This is the function that is called when the mouse is clicked on the span tag
        function settitle(tag, tokenid, owner) {
            const curname = tag.getAttribute("name");
            if (curname == "serial." + tokenid) {
                tag.title = "Owner: " + owner + " Token: " + tokenid;
            } else {
                console.log("Not the same: " + curname + " != " + tokenid);
            }
        }
    
    
        $(document).ready(function () {
            $(".popup").hide();
        });
    
        function connect_opensea(ref){
            ref.onclick = function (e) {
                e.preventDefault();
                var cur_serial = ref.getAttribute("name").split('.')[1];
                $("iframe").attr("src", "https://opensea.io/assets/matic/" + contractid  + "/" + cur_serial + "/");
                $(".links").fadeOut('slow');
                $(".popup").fadeIn('slow');
            };
    
            $(".close").click(function () {
                $(this).parent().fadeOut("slow");
                $(".links").fadeIn("slow");
            });
        }
    
    
        function s(ref) {
    
            //ref.onclick = onclick_async_getowner;
            //ref.onclick = onclick_async_getprice;
            //connect_opensea(ref);
    
            curid = ref.id;
            console.log(ref); 
            var cur_serial = ref.getAttribute("name").split('.')[1];
            serial_num = cur_serial;
    
            return books_nft_handoff(ref, datamine, contractid, network, serial_num);
    
    
            ref.title = "Bookmark: " + serial_num + ", ContactID: " + contractid + ", Network: " + network;
            console.log("Bookmark: " + serial_num + ", ContactID: " + contractid + ", Network: " + network);
    
            ref.onmouseover = function(e) {
                var cur_serial = ref.getAttribute("name").split('.')[1];
                serial_num = cur_serial;
                console.log("Mouse over: " + ref.id);
                curid = ref.id;
            };
    
            html = '<span></span>';
    
    
            emb = document.createElement("div");
            emb.innerHTML = html;
    
            insertAfter(ref, emb.firstChild);
    
    
        }
    
        </script>
        """
    
        return body
    
    
    def recodehtml(self, html, datamine="TLSC"):
       html = html.decode('utf-8', errors="ignore")
    
     
       html = html.replace('<head>', '<head>' + gethead(datamine))
       html = html.replace('</head>', '</head>')
    
       html = html.replace('<body>', '<body>' + getbody(datamine))
       html = html.replace('</body>', '</body>')
    
       html = html.replace('.jpeg', '.jpeg?datamine=' + datamine)
       html = html.replace('.jpg', '.jpg?datamine=' + datamine)
       html = html.replace('.png', '.png?datamine=' + datamine)
       html = html.replace('style.css', 'style.css?datamine=' + datamine)
    
       return html.encode('utf-8')
    
    
    #
    # Calulate the portential of the contract/work of art.
    #
    class Potential():
    
        def __init__(self, datamine, curserial_num, arttype, error_fingerprint):
            self.warning = "BETA! This is a work in progress.  Please report any bugs to the author: johnrraymond@yahoo.com."
            self.datamine = datamine
            self.curserial_num = curserial_num
            self.error_fingerprint = error_fingerprint
    
            self.page = BreadPage.objects.filter(datamine=self.datamine)
    
            self.arttype = arttype
            self.title = self.get_title()
            self.books = self.get_books()
            self.bookmarks = self.get_bookmarks()
            self.cost = self.get_cost()
            self.net = self.get_net()
            self.booksales = self.get_booksales()
            self.bookmark_sales = self.get_bookmarksales()
            self.sales = self.get_total_sales()
    
        def get_bookprice(self):
            try:
                return int(self.page[0].bookprice)
            except:
                self.warning = self.warning + "Using an average book price. "
                return 6
    
        def get_bookmarks(self):
            try:
                return int(self.page[0].maxbookmarksupply)
            except:
                self.warning = self.warning + "No maxbookmarksupply. "
                return 22222
    
        def get_books(self):
            try:
                return int(self.page[0].maxbooksupply)
            except:
                self.warning = self.warning + "No maxbooksupply. "
                return 100000
    
        def get_title(self):
    
            if len(self.page) == 0:
                return "Project is not in the database? ERROR code: SANITY CHECK: " + self.datamine
    
            return self.page[0].title
            
    
        def get_error_fingerprint(self):
            return self.error_fingerprint
    
        def get_datamine(self):
            return self.datamine
    
        def get_curserial_num(self):
            return self.curserial_num
    
        def get_work(self):
            if self.books == -1:
                self.warning = self.warning + "Using average work of ~130,000 tokens per book including bookmarks. "
                return 22222 + 100000       # Average Bookmarks + books
    
            return self.books + self.bookmarks
    
        def get_booksales(self):
            if self.books == -1:
                return 22222 * self.get_bookprice()           # Average Books * book price.
    
            return self.books * self.get_bookprice()      # Books * book price.
    
        def get_bookmarkprice(self):
            return 0                    # TODO: Get this from the database. 6 CB is the default price for a book/mark.
                                        # Effectively, 0 as long as the book is free at the same time as buying the bookmark.
    
        def get_bookmarksales(self):
            if self.books != -1:
                return 22222 * self.get_bookmarkprice()       # Average Bookmarks * book price.
    
            return self.bookmarks * self.get_bookmarkprice()      # Bookmarks * book price.
    
        def get_total_sales(self):
            total_sales = 0
            total_sales += self.get_booksales() 
            total_sales += self.get_bookmarksales()
            return total_sales
    
        def get_cost(self):
            cost = 350                      # Base cost of 350 Cultural Bits. For cover and bookmark art
            cost += 0.1 * self.get_work() # 0.1 CBs per unit of work.
    
            return cost
    
        def get_net(self):
            cost = self.get_cost() 
            roi = self.get_total_sales()
            net = roi - cost
    
            return net
    
    
    def calculate_project_potential(datamine, curserial_num, arttype, returntype="object", error_fingerprint="SUCCESS"):
        potential = Potential(datamine, curserial_num, arttype, error_fingerprint)
    
        if returntype == "json":
            return json.dumps(potential.__dict__, default=lambda o: 'coded')
    
        return potential
    
    
    
    
    def jrreditor_get_current_html(potential, cur_serial):
        dataminedir = books.datamine_path(potential.datamine)
        indexfile = books.datamine_get_index(dataminedir)
        bookmarkfile = books.datamine_get_bookmark(dataminedir)
    
    
        bytesperbookmark = 33
        try:
            btyesperbookmark = int(potential.page[0].bperbookmark)
            study.doresidual("jrre-index.html", cur_serial, bytesperbookmark, dataminedir )
        except:
            pass
    
    
        study = Study("jrre-index.html", bytesperbookmark, cur_serial, dataminedir + "/")
        study.makeart(int(cur_serial))
    
        print("study is done")
    
        print("starting to mint the book's smart contrtact.")
    
        return "study done" + str(cur_serial)
    
    
    
    
    def jrreditor_get_art_html(potential, cur_serial, arttype):
    
        if(potential.page[0].curserial_number < cur_serial):
            potential.warning = potential.warning + "The current serial number is higher than the serial number in the database. "
            throw("The current serial number is higher than the serial number in the database.")
    
        html = jrreditor_get_current_html(potential, cur_serial);
    
        return html
    
    
    # Create your views here.
    def art(request):
        arttype = request.GET.get('type', 'book')
        curserial_num = request.GET.get('curserial_num', '10')
        curserial_num = re.sub(r'[^a-zA-Z0-9\.]', '', curserial_num)
        datamine = request.GET.get('datamine', 'TLSC')
        datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)
    
        if arttype == 'book':
            arthtmlfilename = 'art/datamines/' + datamine + '/' + datamine + '.nft/' + 'index.html.' +  curserial_num + '.html'
            curhtmlfilename = '/home/john/' + datamine + '/' + datamine + '.nft/' + 'index.html.' +  curserial_num
    
            #f = gzip.open(curhtmlfilename, 'rb')
    
            if not exists(curhtmlfilename + ".html"):
                try:
                    f = gzip.open(curhtmlfilename, 'rb')
                    html = f.read()
                    f.close()
                except:
                    potential = calculate_project_potential(datamine, curserial_num, "book", error_fingerprint=curhtmlfilename)
                    if not os.path.exists('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine):
                        lock = FileLock("high_ground.txt.lock")
                        with lock:
                            shutil.move('/home/john/' +datamine, '/mnt/volume_nyc1_01/')
                            os.symlink('/mnt/volume_nyc1_01/' + datamine, '/home/john/' + datamine)
    
    
                    if potential.page[0].usejrreditor:
                        jrreditor_artname = 'art/datamines/' + datamine + "/jrre-index.html.nft/index.html."+curserial_num+".html"
                        if not exists(jrreditor_artname):
                            potential.warning = potential.warning + "The jrreditor art file does not exist. "
                            print("The jrreditor art file does not exist. ")
                            
                            jrreditor_get_art_html(potential, curserial_num, "book")
    
    
    
                        #f = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/jrre-index.html.nft/index.html.' +  curserial_num + '.html', "w")
    
                        #f = gzip.open("/home/john/" + datamine + "/" + datamine + ".nft/index.html." + curserial_num, 'wb')
                        f = gzip.open("/home/john/" + datamine + "/jrre-index.html.nft/index.html." + curserial_num, 'rb')
                        html = f.read()
                        f.close()
    
                        # We have the art!!! First time on the jrreditor side of the house.
                        html = recodehtml(potential, html, datamine)
                        f = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/jrre-index.html.nft/index.html.' +  curserial_num + '.html', "wb")
                        f.write(html)
                        f.close()
    
    
                
                        return render(request, jrreditor_artname, get_serials(curserial_num))
                        
                        try:
                            pass
                        except:
                            retjson = calculate_project_potential(datamine, curserial_num, "book", returntype="json", error_fingerprint="Can't do something in jrreditor")
                            return render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})
    
                        return HttpResponse(html)
                    else:
                        retjson = json.dumps(potential.__dict__, default=lambda o: 'coded')
                        return render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})
    
                html = recodehtml(html, datamine)
    
                f = open(curhtmlfilename + ".html", 'wb')
                f.write(html)
                f.close()
    
            return render(request, arthtmlfilename, get_serials(curserial_num))
    
        elif arttype == 'bookmark':
            response = FileResponse(content_type="image/jpeg")
            curbookmark = '/home/john/' + datamine + '/' + datamine + '.nft/choicetext.' +  curserial_num + ".jpg"
            try:
                img = open(curbookmark, "rb")
            except:
                json = calculate_project_potential(datamine, curserial_num, "bookmark", returntype="html", error_fingerprint=curbookmark)
                return json
    
            response = FileResponse(img)
            return response
            
    
    def price(request):
        datamine = request.GET.get('datamine', 'TLSC')
        tokenid = request.GET.get('tokenid', '0')
        datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)
    
        contractid = getcontractid(datamine)
    
        #fh = urllib.request.urlopen('https://opensea.io/assets/matic/' + contractid  + '/' + tokenid)
        #html = fh.read()
        #fh.close()
    
        html = 'https://opensea.io/assets/matic/' + contractid  + '/' + tokenid
        #html = 'https://opensea.io/assets/matic/' + contractid  + '/' + tokenid
    
        return HttpResponse(html)
    
    
    def images(request):
        datamine = request.GET.get('datamine', 'TLSC')
        path = request.path
        path = path.replace('art/', '/')
    
        response = FileResponse(content_type="image/jpeg")
        img = open("/home/john/" + datamine + path, "rb")
        response = FileResponse(img)
        return response
    
    def styles(request):
        datamine = request.GET.get('datamine', 'TLSC')
        response = FileResponse(content_type="text/css")
        img = open("/home/john/" + datamine + "/style.css", "rb")
        response = FileResponse(img)
        return response
