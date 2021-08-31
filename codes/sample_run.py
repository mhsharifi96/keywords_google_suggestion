from g_search import main as g_main
import  time
import configparser
from wordcloud_conventor import wordcloud_conventor
import os
rec_file_name = 'rec'+str(int(time.time()))+"_a28_ir.txt"
rel_file_name = 'rel'+str(int(time.time()))+"_a28_ir.txt"
keyword = 'خرید گلاب'
res_rec,res_rel = g_main(search_val=keyword,rec_search_dir=rec_file_name,rel_word_search_dir=rel_file_name) 
# res_rec,res_rel = g_main(search_val='گلاب') 
# TODO : check rel_file_name sometime not avaiable
if os.path.isfile(rel_file_name):
    with open(rec_file_name, 'a') as outfile:
        with open(rel_file_name) as infile:
            for line in infile:
                outfile.write(line)
        #     infile.close()
        outfile.close


wordcloudFileName = wordcloud_conventor(fileLocation=rec_file_name)
print('finishing :)')