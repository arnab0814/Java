'''Async IO in Python'''

# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

# Syntax
# Here is the basic syntax for creating an asynchronous function in Python:
'''
import asyncio
async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"
async def main():
    result = await my_async_function()
    print(result)
asyncio.run(main())
'''

# Another way to schedule tasks concurrently is as follows:
'''
L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
print(L)'''

# Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.



# CODE 


# import asyncio 
# import requests


# async def function1():
#   print("func 1") 
#   URL = "https://c4.wallpaperflare.com/wallpaper/297/22/531/lake-blue-moonlight-moon-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("image1.jpg", "wb").write(response.content)
   
#   return "Harry"
  
# async def function2():
#   print("func 2") 
#   URL = "https://c4.wallpaperflare.com/wallpaper/297/22/531/lake-blue-moonlight-moon-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("image2.jpg", "wb").write(response.content)
  
# async def function3():
#   print("func 3")
#   URL = "https://c4.wallpaperflare.com/wallpaper/168/544/889/moonlight-nature-digital-art-moon-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("image3.jpg", "wb").write(response.content)

# async def main():
#   await function1()
#   await function2()
#   await function3()

# #   L = await asyncio.gather(
# #         function1(),
# #         function2(),
# #         function3(),
# #     )
# #   print(L)



# #   task = asyncio.create_task(function1())
# #   await function1()
# #   await function2()
# #   await function3()

# asyncio.run(main())


# MY CODE


import asyncio
# import time
import requests

# NOTE:- THIS WORKS WHEN WE WANT TO DOWNLOAD CONTENT FROM ONLINE

async def function1():
    
    url = "https://c4.wallpaperflare.com/wallpaper/297/22/531/lake-blue-moonlight-moon-wallpaper-preview.jpg"
    data = requests.get(url)
    open("image1.jpg","wb").write(data.content)
    

async def function2():

    url = "https://c4.wallpaperflare.com/wallpaper/297/22/531/lake-blue-moonlight-moon-wallpaper-preview.jpg"
    data = requests.get(url)
    open("image2.jpg","wb").write(data.content)
    

async def function3():

    url = "https://c4.wallpaperflare.com/wallpaper/168/544/889/moonlight-nature-digital-art-moon-wallpaper-preview.jpg"
    data = requests.get(url)
    open("image3.jpg","wb").write(data.content)
    
      

async def main():
    
# THIS RUNS FUNCIONS 1 BY 1, Since await makes the function run and wait

    # await function1()
    # print("fuction1")
    
    # await function2()
    # print("fuction2")
    
    # await function3()
    # print("fuction3")
    
    
    
# THIS RUNS ALL FUNCNTION TOGETHER
 
    run = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    return run

asyncio.run(main())