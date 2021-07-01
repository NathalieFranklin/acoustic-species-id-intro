import pandas as pd
import csv
import random





def randomixer(value,file,writer):

    row_list = []
    index =0
    for row in value:

      random_index =random.choice(value[row])

      for x in file:

          row_list.append(file[x][random_index])


      if (row_list==[]):
        continue
      writer.writerow(row_list)
      row_list.clear()
      index= index +1



def stratalizer ():
    can_open_file= True

    try:
        file = pd.read_csv('Peru_2019_AudioMoth_Data_Full.csv',)

    except FileNotFoundError as e:

        can_open_file= False
        return can_open_file

    f = open('stratilized_data.csv', 'w',newline='')
    writer = csv.writer(f)
    audio_moth_header = []
    am_list =[]
    row_list = []
    dic_times_index={}
    index=0


    for row in file:
        audio_moth_header.append(row)
        writer.writerow(audio_moth_header)
    for row in file['AudioMothCode']:
       duration = file['Duration'][index]
       time= str(file['Comment'][index])[12:14]

       if (time== ''):
          index= index +1
          continue

       if (row not in row_list):

            row_list.append(row)


            if(len(am_list)==24):
                randomixer(dic_times_index,file,writer)
            dic_times_index ={}
            am_list.clear()
       if (duration>60.00 and (time not in am_list)):
            am_list.append(time)

                 #dic_index[row]= dic_times_index
       if (time not in dic_times_index):
           dic_times_index[time]= []

       dic_times_index[time].append(index)
       index = index+1




    return can_open_file

#stratalizer()

f.close()
                              
