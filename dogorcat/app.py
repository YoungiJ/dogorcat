__all__=['is_cat','learn','classify_image','categories','image','label','examples','intf']
# In[4]:

from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()


learn=load_learner('model.pkl')
#학습모델>> 이미 저장되어 있음 frozen object> unfreeze


# In[11]:
categories=('Dog','Cat')

def classify_image(img):
    pred,idx,probs=learn.predict(img)
    return dict(zip(categories,map(float,probs)))
# gradio는 pytorch는 tensor로 반환하지 numpy array로 반환하지 않는다
# 모든걸 float으로 바꿔줘야함


image=gr.inputs.Image(shape=(192,192))
label=gr.outputs.Label()
examples=['dog.jpg','cat.jpg','bird.jpg']

intf=gr.Interface(fn=classify_image,inputs=image,outputs=label,examples=examples)
intf.launch(inline=False)