import urllib.request

url = input("Entre com o site para a busca: ")
nivel = int(input("Nível de profundidade da busca: "))

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
)
webpage = urllib.request.urlopen(req)

def Buscar(f,n,esp):
    for x in f:
        if b'href="https:' in x:
            pos = x.find(b'href="https:')
            while pos != -1:
                pos_begin = pos + 6
                pos_end = pos_begin + x[pos_begin:].find(b'"')
                print(esp , x[pos_begin:pos_end])
                if(n > 0):
                    e = esp
                    e = e + "    " 
                    url = x[pos_begin:pos_end].decode("utf-8")
                    req = urllib.request.Request(
                        url, 
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'} 
                    )
                    w = urllib.request.urlopen(req)
                    Buscar(w,n - 1,e)
                x = x[pos + 6:]
                pos = x.find(b'href="https:')
            
Buscar(webpage,nivel,"")
        
        
            

