#!/usr/bin/python3

import os, sys
import subprocess
import argparse
import roots
import numpy as np
#from pydub import AudioSegment

from scipy.io import wavfile
#fs, data = wavfile.read('./output/audio.wav')

def extract_start_end_time(item, segment_sequence_name):
	
	seg_items = item.get_related_items(segment_sequence_name)
	
	if len(seg_items) == 0:
		s1 = 0
		s2 = 0
	else:
		seg_start=[]
		seg_end=[]
		for seg_item in seg_items:
			seg_new_item = seg_item.as_acoustic_Segment()
			seg_start.append(seg_new_item.get_segment_start())
			seg_end.append(seg_new_item.get_segment_end())
		s1 = seg_start[0]
		s2 = seg_end[-1]
	#print(seg_start, seg_end)
	return s1, s2

def write_wav_text_data(dirname, roots_file, out_file):
	fo = open(out_file, 'a')
	
	#outputIpaAlphabet = roots.phonology_ipa_Ipa()
	#basename = dirname + '/' + roots_file
	basename = dirname + roots_file
	corpus = roots.Corpus(basename)
	nutts = corpus.count_utterances()
	#basename, ext = os.path.splitext(roots_file)
	basename_ = dirname + '/'
	#dirname, filename = os.path.splitext(roots_file)
	
	for utt_index in range(0, nutts):#niveau paragraphe ?
		try:
			utt = corpus.get_utterance(utt_index)
		except:
			continue
		signal_sequence = utt.get_sequence('Signal').as_segment_sequence()
		signal_item = signal_sequence.get_item(0).as_acoustic_SignalSegment()
		try:
			fs, signal_full = wavfile.read(basename_  + signal_item.to_string(1))
		except:
			continue
		#sentence_seq = utt.get_sequence('Character Label')
		#if len(sentence_seq.to_string()) == 0:
			#continue
		#print(seq_sentence.to_string())
		#word_JTrans_seq = utt.get_sequence('Word JTrans')
		#print(word_JTrans_seq.to_string())
		
		#word_item0 = word_JTrans_seq.get_item(0)
		#start_time0, end_time0 = extract_start_end_time(word_item0, 'Time Segment JTrans')
		#num_sentence = 0
		#text1 = word_item0.to_string()wavs/
		
		word_raw_seq = utt.get_sequence('Word Raw')
		#print(word_raw_seq.to_string())
		word_raw_nb = word_raw_seq.count()
		text2 = []
		raw = ''
		for k in range(word_raw_nb):
			
			word_raw_string = word_raw_seq.get_item(k).to_string()
			#print(':::', word_raw_string)
			#raw = raw + ' ' + word_raw_string
			if word_raw_string == '':
				continue
			if k < word_raw_nb -1:
				if ((word_raw_string[-1] == '.') | ('.]' in word_raw_string) | ('],' in word_raw_string) | ('[[' in word_raw_string) | ('?' in word_raw_string) | (word_raw_string == '...') | ('...' in word_raw_string) | ('…' in word_raw_string) | ('.)' in word_raw_string) | ('!...' in word_raw_string)) & ((word_raw_string != 'M.') & (word_raw_string != '?...') & ('.]...' not in word_raw_string) & (word_raw_string != '?…')):
					#print("(word_raw_string)",word_raw_string)
					raw = raw + ' ' + word_raw_string
					text2.append(raw)
					#print("# (text2):",text2)
					raw = ''
				elif (word_raw_string == '?...') | (word_raw_string == '?…'):
					raw = raw + ' ?'
					text2.append(raw)
					raw = '...'
					text2.append(raw)
					raw = ''
				elif ']...' in word_raw_string:
					raw = raw + ']'
					text2.append(raw)
					raw = '...'
					text2.append(raw)
					raw = ''
				elif word_raw_string == '[Note':
					if raw != '': text2.append(raw)
					raw = word_raw_string
				elif ('note.]' in word_raw_string) | ('note]' in word_raw_string):
					raw = raw + ' ' + word_raw_string
					text2.append(raw)
					raw = ''
				elif word_raw_string == 'fusil.Il':
					raw = raw + ' fusil.'
					text2.append(raw)
					raw = 'Il'
				elif word_raw_string == 'roi.Les':
					raw = raw + ' roi.'
					text2.append(raw)
					raw = 'Les'
				#elif word_raw_string == 'Introduction.)':
					#raw = raw + ' ' + word_raw_string
					#text2.append(raw)
					#raw = ''
				elif word_raw_string == "Provinces[Note":
					raw = raw + ' Provinces'
					text2.append(raw)
					raw = '[Note'
				elif word_raw_string == "four[Note":
					raw = raw + ' four'
					text2.append(raw)
					raw = '[Note'
				#elif (raw == " Je le conçois, les apparences ont pu") & (word_raw_string == 'te'):
					#del(text2[-1])
					#raw = '– Non... ' + raw
				else:
					raw = raw + ' ' + word_raw_string
			else:
				raw = raw + ' ' + word_raw_string
				text2.append(raw)
			
		print(word_raw_seq.to_string())
		#print(text2)
		#sys.exit()
		
		word_seq = utt.get_sequence('Word JTrans')
		word_item0 = word_seq.get_item(0)
		phone_items0 = word_item0.get_related_items('Phone JTrans')
		start_time0, end_time0 = extract_start_end_time(word_item0, 'Time Segment JTrans')
		num_sentence = 0
		text1 = word_item0.to_string()
		phone_seq_string = ' '.join([phone_item.to_string() for phone_item in phone_items0])
		text3 = phone_seq_string
		
		word_item_nb = word_seq.count()
		
		for word_index in range(1, word_item_nb):
			word_item = word_seq.get_item(word_index)
			word_string = word_item.to_string()
			
			phone_items = word_item.get_related_items('Phone JTrans')
			phone_item = ' '.join([phon.to_string() for phon in phone_items])
			#print(word_string, text1)
			#text1 = text1 + ' ' + word_string
			
			#if text1 == " la nuit était noire , le quartier .":
				#continue
			#if text1 == "ferme l' châssis mon enfant , dit la mère Morlaix , après un instant de .":
				#continue
			#if text1 == "le gardien était en effet pensif et .":
				#continue
			#if text1 == "Ã‰zÃ©chiel restait .":
				#continue
			#if text1 == " la porte se referma , et la maison redevint .":
				#continue
			#if text1 == "il y eut encore un .":
				#continue
			#if text1 == "demanda René de Kervoz après un long .":
				#continue
			#print('--', text1, ':', word_string)
			if text1 + word_string == '.':
				continue
			if word_index < word_item_nb - 1:
				#print(word_index, '/', word_item_nb)
				word_next = word_seq.get_item(word_index + 1).to_string()
				#print(word_next)
				if ('silenc' in word_next):
					continue
			if (word_string in ['.', '?', '...', '?...']):
				text1 = text1 + ' ' + word_string
				text3 = text3 + '§' + phone_item
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1 (JTrans):',text1)
				#print('2 (Raw):',text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)# | ('Silenc' in word_next):
				
				start_time0 = end_time1
				num_sentence += 1
				text1 = ''
				text3 = ''
			elif (word_string == 'Note') & (word_next == ':'):
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1:', text1)
				#print('2:', text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)
				
				start_time0 = end_time1
				num_sentence += 1
				text1 = 'Note'
				text3 = 'n O t @'
			elif (text1 == ' fin de la') & ((word_string == 'note') | (word_string == 'note.')):
				text1 = text1 + ' ' + word_string
				text3 = text3 + '§' + phone_item
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1:', text1)
				#print('2:', text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)
				
				start_time0 = end_time1
				num_sentence += 1
				text1 = ''
				text3 = ''
			elif word_index == word_item_nb -1:
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1:', text1)
				#print('2:', text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)
			elif (word_string == 'phrantsesos') & (text1 == " à Chalcis j' ai eu l' honneur d' être annoncé comme un milordos"):
				text1 = text1 + ' ' + word_string
				text3 = text3 + '§' + phone_item
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1:', text1)
				#print('2:', text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)
				start_time0 = end_time1
				num_sentence += 1
				text1 = ''
				text3 = ''
			elif (word_string == 'camarades') & (text1 == "Note :") & (word_next == ','):
				text1 = text1 + ' ' + word_string
				text3 = text3 + '§' + phone_item
				start_time1, end_time1 = extract_start_end_time(word_item, 'Time Segment JTrans')
				signal_sentence_values = signal_full[int(start_time0*fs):int(end_time1*fs)]
				
				#print('1:', text1)
				#print('2:', text2[num_sentence])
				wavname = 'SynPaFlex_' + roots_file[0:-16] + '_' + str(utt_index) + '_' + str(num_sentence) + '.wav'
				fo.write(wavname + '|' + text1 + '|' + text2[num_sentence] + '|' + text3 + '\n')
				wavfile.write("/lium/raid01_b/tgranjon/synpaflex/wavs/" + wavname, fs, signal_sentence_values)
				start_time0 = end_time1
				num_sentence += 1
				text1 = ''
				text3 = ''
			else:
				text1 = text1 + ' ' + word_string
				text3 = text3 + '§' + phone_item
			word_item.destroy()
		#sys.exit()
		#utt.destroy()
	#print('---done corpus')
	fo.close()


def main():
	parser = argparse.ArgumentParser(description='Create wavfiles and metadata from SynPaFlex corpus')
	parser.add_argument('dir_file', type=str, help='directory where roots files are located)')
	parser.add_argument('out_file', type=str, help='output csv file name)')
	#parser.add_argument('seq_name', type=str, help='name of the sequence to extract')
	

	args = parser.parse_args()

	#dir_file = args.dir_file
	out_file = args.out_file
	
	filenames = os.listdir(args.dir_file)
	
	#roots_file = 'chevalier_filledupirate_097_acoustic.json'
	#roots_file = 'chevalier_filledupirate_067_acoustic.json'
	#roots_file = 'feval_vampire_05_acoustic.json'
	#roots_file = 'feval_vampire_09_acoustic.json'
	#roots_file = 'andersen_contes_02_03_acoustic.json'
	
	for roots_file in sorted(filenames):
		#if roots_file < 'sue_mysteresdeparis_01_13_acoustic.json':
			#continue
		#if '_acoustic.json' in roots_file:
		if '_full_final.json' in roots_file:
			print('--->', roots_file)
			write_wav_text_data(args.dir_file, roots_file, out_file)
			#sys.exit()
	
	#print('Mean value for sequence {0}: {1}'.format(seq_name, np.mean(D)))
	#print('mean value={0}, std value={1}'.format(np.mean(D), np.std(D)))
	

########################################################################


if __name__ == "__main__":
	main() 
