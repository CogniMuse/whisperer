import argparse
import csv
import os
import time
import whisper


def run_whisper():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-i","--input",
                            help="File or folder address which contains the audio/video files to be transcribed",required=True)
    
    arg_parser.add_argument("-o","--output",           
                            help="Output directory for the transcriptions")
    
    arg_parser.add_argument("-m","--model",
                            help="Select one of the whisper models. default model is base")
    
    arg_parser.add_argument("-l","--language",
                            help="Select the the language of the content to be transcribed. Default is English")

    args = arg_parser.parse_args()

    
    supported_formats = ['mp3','wav','flac']

    if os.path.isdir(args.input):
        for file in os.listdir(args.input):
            if file.split('.')[-1] in supported_formats:
                print("Transcribing: ",file)
                transcribe(args.input+'/'+file,args.output,args.model)
    
    else:
        if os.path.isfile(args.input):
            if args.input.split('.')[-1] in supported_formats:
                transcribe(args.input,args.output,args.model)

        print ("Input a supported audio format. Supported formats are Mp3, Wav and FLAC")

def transcribe(audio_file,output,model):

    try:
        start_time = time.time()
        whisper_model = whisper.load_model("base")
        transcription = whisper_model.transcribe(audio=audio_file,fp16=True,verbose=True)
    
        end_time = time.time()

        total_time = end_time - start_time

        with open(output+'/'+audio_file.split('/')[-1]+'.txt' if output is not None else audio_file+'.txt','w',encoding='utf-8') as f:
            f.write(transcription['text'])
        
        with open(output+'/'+audio_file.split('/')[-1]+'_SEGMENTS'+'.csv' if output is not None else audio_file+'_SEGMENTS','w',newline='') as s:
            w = csv.DictWriter(s,['id','seek','start','end','text','tokens'])
            w.writeheader()
            for x in transcription['segments']:
                w.writerow(rowdict={
                    'id':x['id'],
                    'seek':x['seek'],
                    'start':x['start'],
                    'end':x['end'],
                    'text':x['text'],
                    'tokens':x['tokens']
                })

        print(' Completed in ',total_time, 'seconds')
        del whisper_model
        del transcription

    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    run_whisper()

