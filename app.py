import numpy as np
import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
#에휴
#에휴휴
#엫휴휴ㅠ흏ㄴㅇㄹㄴㅇㅇㄹㅇㄴㅇㅊㄴㅇ