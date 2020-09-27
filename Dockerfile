FROM fastdotai/fastai:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
RUN pip install -Uqq fastbook 
EXPOSE 33507 
CMD ["python","-u","main.py"]