import asyncio
import requests

def fun1():
    url = "https://images.pexels.com/photos/378570/pexels-photo-378570.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    res = requests.get(url)
    open("insta.jpg","wb").write(res.content)
    print("fun1")
def fun2():
    url = "https://images.pexels.com/photos/2028885/pexels-photo-2028885.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    res = requests.get(url)
    open("insta1.jpg","wb").write(res.content)
    print("fun2")
def fun3():
    url = "https://images.pexels.com/photos/572861/pexels-photo-572861.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    res = requests.get(url)
    open("insta2.jpg","wb").write(res.content)
    print("fun3")
    
async def main():
    # fun1()
    # fun2()
    # fun3()
    l = await asyncio.gather(fun1,fun2,fun3)
    print(l)
    
asyncio.run(main())