platform_body = """
import csv
import bottle
import json
import os
import random
import re
import sqlite3
import sys
from bottle import request
from beaker.middleware import SessionMiddleware

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import config
import model

bottle.debug(True)

views_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views/')
bottle.TEMPLATE_PATH.insert(0, views_path)
app = bottle.Bottle()

app.config['myapp.APP_PREFIX'] = model.get_prefix()

session_opts = {
	'session.type': 'file',
	'session.cookie_expires': False,
	'session.data_dir': os.path.join(os.path.dirname(os.path.abspath(__file__)),'data'),
	'session.auto': True
}

app_middlware = SessionMiddleware(app, session_opts)
app_session = bottle.request.environ.get('beaker.session')

@app.route('/')
def badroute():
	book = model.get_book_variable_module_name('config')
	data={'APP_PREFIX':request.app.config['myapp.APP_PREFIX'], 'config': book}
	return bottle.template('index', data)

@app.route('/login')
@app.post('/login')
def login():
	mail = post_get('email')
	pattern='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
	if not re.match(pattern,mail) :
		book = model.get_book_variable_module_name('config')
		data={'APP_PREFIX':request.app.config['myapp.APP_PREFIX'], 'config': book, 'error' : 'Invalid email address'}
		return bottle.template('index', data)
	app_session = bottle.request.environ.get('beaker.session')
	app_session['logged_in'] = True
	app_session['pseudo'] = mail
	bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/test')

@app.route('/logout')
@app.post('/logout')
def logout():
	bottle.request.environ.get('beaker.session').delete()
	bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/')

@app.route('/login')
def toto():
	app_session = bottle.request.environ.get('beaker.session')
	if('pseudo' in app_session) :
		return '<p>You are already logged, please logout <a href="'+request.app.config['myapp.APP_PREFIX']+'/logout">here</a></p>'
	book = model.get_book_variable_module_name('config')
	data={'APP_PREFIX':request.app.config['myapp.APP_PREFIX'], 'config': book}
	return bottle.template('index', data)

# Bottle post methods
def postd():
	return bottle.request.forms

def post_get(name, default=''):
	return bottle.request.POST.get(name, default).strip()

def testLogin():
	app_session = bottle.request.environ.get('beaker.session')
	if 'pseudo' in app_session:
		return True
	else:
		return False

def encode_system(syst) :
	#proceede to the encoding of your system name here so it won't apear clearly in source code
	return str(syst)

def decode_system(syst) :
	#reverse operation of previous one
	return str(syst)

@app.route('/test')
def process_test():
	app_session = bottle.request.environ.get('beaker.session')
	#the following lines are to be uncommented later
	if not testLogin() :
		bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/login')
	user = app_session['pseudo']
	#proceed to the test
	#check if the test isn't finished yet
	if model.get_nb_step_user(user) < model.get_nb_step() :
		#proceed to a new step
		book = model.get_book_variable_module_name('config')
		if model.get_nb_intro_steps() > 0 and model.get_nb_step_user(user) == 0 and not 'intro_done' in app_session:
			if not 'nb_intro_passed' in app_session:
				app_session['nb_intro_passed'] = 0
			(samples, systems, index) = model.get_intro_sample(user)
			(samp, sys, ind) = model.get_trans_sample(user)
			enc_systems = []
			for s in systems :
				enc_systems.append(encode_system(s))
			hidden = '<input type="hidden" name="ref" value="'+str(index)+'">'
			j=0
			for s in enc_systems :
				hidden = hidden + '<input type="hidden" name="real_system_'+str(j)+'" value="'+s+'">'
				j=j+1
			data={"APP_PREFIX":request.app.config['myapp.APP_PREFIX'], "samples":samples, "systems":enc_systems, "nfixed": model.get_nb_position_fixed(), "index":index, "samp":samp, "sys":sys, "ind":ind, "user":user, "introduction": True, "step": app_session['nb_intro_passed']+1, "totalstep" : model.get_nb_intro_steps(), "progress" : (100*(app_session['nb_intro_passed']+1))/model.get_nb_intro_steps(), "config": book, "hidden_fields": hidden}
		else:
			(samples, systems, index) = model.get_test_sample(user)
			(samp, sys, ind) = model.get_trans_sample(user)
			enc_systems = []
			for s in systems :
				enc_systems.append(encode_system(s))
			hidden = '<input type="hidden" name="ref" value="'+str(index)+'">'
			j=1
			for s in enc_systems :
				hidden = hidden + '<input type="hidden" name="real_system_'+str(j)+'" value="'+s+'">'
				j=j+1
			book = model.get_book_variable_module_name('config')
			data={"APP_PREFIX":request.app.config['myapp.APP_PREFIX'], "samples":samples, "systems":enc_systems, "nfixed": model.get_nb_position_fixed(), "index":index, "samp":samp, "sys":sys, "ind":ind, "user":user, "introduction": False, "step": model.get_nb_step_user(user)+1, "totalstep" : model.get_nb_step(), "progress" : model.get_progress(user), "config": book, "hidden_fields": hidden}
		return bottle.template('template', data)
	else :
		bottle.request.environ.get('beaker.session').delete()
		return "<p>You have already done this test</p>"

@app.post('/test')
def process_test_post():
	process_answers()

@app.post('/answer')
def process_answers():
	app_session = bottle.request.environ.get('beaker.session')
	if not 'nb_intro_passed' in app_session:
		app_session['nb_intro_passed'] = 0
	if model.get_nb_intro_steps() == 0 and app_session['nb_intro_passed'] == 0:
		app_session['intro_done'] = True
	#the following lines are to be uncommented later
	if not testLogin() :
		bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/login')
	user = app_session['pseudo']
	#get the post data and insert into db
	if ('intro_done' in app_session and app_session['intro_done'] == True) or model.get_nb_step_user(user) > 0:
		systems=[]

		s=1
		while post_get("real_system_"+str(s))!="" :
			systems.append(post_get("real_system_"+str(s)))
			s=s+1
		answers=[]

		i=1
		while post_get("answer_"+str(i))!="" :
			system_index = 1
			question_index = i
			content = post_get("answer_"+str(i))
			if "system_index_"+str(i) in bottle.request.POST:
				system_index = post_get("system_index_"+str(i))
			if "question_index_"+str(i) in bottle.request.POST:
				question_index = post_get("question_index_"+str(i))
			answers.append({"system_index": system_index, "question_index": question_index, "content": content, "sys_index": post_get("sys_index")})
			i=i+1
		post_data = {"author":model.get_author(),"user":user,"answers": answers,"systems": systems,"sample_index": post_get("ref"),"samp_index": post_get("trans"), "question_index": question_index}
		model.insert_data(post_data)
	else:
		app_session['nb_intro_passed'] += 1
		if (app_session['nb_intro_passed'] >= model.get_nb_intro_steps()):
			app_session['intro_done'] = True
	#check if the test isn't finished yet
	if model.get_nb_step_user(user) < model.get_nb_step() :
		bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/test')
	else :
		book = model.get_book_variable_module_name('config')
		data={"APP_PREFIX":request.app.config['myapp.APP_PREFIX'], "config": book}
		bottle.request.environ.get('beaker.session').delete()
		return bottle.template('completed', data)

@app.route('/export')
def export_db():
	book = model.get_book_variable_module_name('config')
	data={'APP_PREFIX':request.app.config['myapp.APP_PREFIX'], 'config': book}
	return bottle.template('export',data)

@app.post('/export')
def export_db_ok():
	if(post_get('token')==model.get_token()):
		if post_get('type') == "DB" :
			return bottle.static_file('data.db', root=os.path.dirname(os.path.abspath(__file__)),download='data.db')
		elif post_get('type') == "CSV" :
			#get the list of systems
			systems= []
			for i in range(1,model.get_nb_system_display()+1):
				systems.append('System num '+str(i))
			with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.csv'), 'w') as csvfile:
				fieldnames = ['user', 'date', 'content', 'system index', 'sample index', 'question index']
				fieldnames = fieldnames + systems
				writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=fieldnames)
				writer.writeheader()
				#query the answers on the db from the model
				answers = model.get_answers()
				sys = model.get_systems()
				for a in answers :
					ct_value = ""
					if not a[4] is None:
							ct_value = sys[int(a[4])]
					row = {'user': a[1], 'date': a[2], 'content': a[3], 'system index': ct_value, 'sample index': a[5], 'question index': a[6]}
					#'system1': sys[int(a[7])], 'system2': sys[int(a[8])], 'system3': sys[int(a[9])], 'system4': sys[int(a[10])], 'system5': sys[int(a[11])]
					i=0
					for s in systems :
						row[s] = sys[int(a[7+i])]
						i+=1
					writer.writerow(row)
			return bottle.static_file('db.csv', root=os.path.dirname(os.path.abspath(__file__)),download='db.csv')
		else :
			return "wrong !"
	else:
		book = model.get_book_variable_module_name('config')
		data={'APP_PREFIX':request.app.config['myapp.APP_PREFIX'], 'config': book, 'error': 'Bad Token !'}
		return bottle.template('export',data)

# Access to local static files
@app.route('/static/:type/:filename#.*#')
def send_static(type, filename):
	return bottle.static_file(filename, root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static/%s/') % type)

# Access to local static media files
@app.route('/media/:filename#.*#')
def send_static(filename):
	return bottle.static_file(filename, root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'media/'))

# # Access to local static sound files
# @app.route('/media/:media/:syst/:filename#.*#')
# @app.route('/media/:media/./:syst/:filename#.*#')
# def send_static(media, syst, filename):
# 	return bottle.static_file(filename, root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'media/%s/') % media+'/'+syst)

@app.route('/:badroute')
def badroute(badroute):
	bottle.redirect(request.app.config['myapp.APP_PREFIX']+'/test')

def main():
	bottle.run(app_middlware, host='kuat.univ-lemans.fr', port=8080, server='paste', reloader=True)
if __name__ == '__main__':
	main()
else:
	application = app_middlware
"""


model_body="""import os
import sqlite3
from datetime import date, datetime
import random
import sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import config
import itertools
import operator

def get_nb_system() :
	# Return the number of sample for a test!
	conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.db'))
	c = conn.cursor()
	c.execute('select count(*) from system')
	res = c.fetchall()
	conn.close()
	return int(res[0][0])

def get_book_variable_module_name(module_name):
	module = globals().get(module_name, None)
	book = {}
	if module:
		book = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
	return book

def get_prefix():
	return config.prefix

def get_token():
	return config.token

def get_headers():
	return config.headersCSV

def get_media():
	return config.useMedia

def get_nb_intro_steps():
	return int(config.nbIntroductionSteps)

def get_nb_position_fixed():
	return int(config.nbFixedPosition)

def get_nb_system_display() :
	return int(config.nbSystemDisplayed)

def get_author():
	# Get it from config.py
	return config.author

def get_questions_type():
	# Get the text of questions as an array
	return config.questionsType

def get_description():
	# Get it from config.py
	return config.description

def get_name():
	# Get it from config.py
	return config.name

def get_nb_step() :
	# Return the number of step required on a test
	# Get it from config.py
	return int(config.nbSteps)

def get_nb_step_user(user) :
	# Return the number of step made by a user on the test
	conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.db'))
	c = conn.cursor()
	c.execute('select count(*) from answer where user="'+user+'"')
	#c.execute('select count(distinct(sample_index)) from answer where user="'+user+'"')
	res = c.fetchall()
	conn.close()
	return int(res[0][0]/2)

def get_progress(user):
	# Return the ratio of steps achieved by the user over the total number of steps
	return 100*(get_nb_step_user(user)+1)/get_nb_step()

def get_metadata() :
	# Get it from config.py
	metadata=dict()
	for i in dir(config):
		# i,'  ',getattr(config,i)
		b = re.search(r'__.+__',str(i))
		if not b:
			metadata[str(i)]=getattr(config,i)
	return metadata

def get_answers() :
	conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.db'))
	c = conn.cursor()
	c.execute('select * from answer')
	answers = c.fetchall()
	conn.close()
	return answers

def get_systems() :
	conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.db'))
	c = conn.cursor()
	c.execute('select * from system')
	systems = c.fetchall()
	conn.close()
	sys={}
	for s in systems :
		sys[s[0]] = s[1]
	return sys

def get_shuffled_list_of_system_ids(nbFixed, connection) :
	# Build the list of system IDs such that fixed position systems are returned in priority,
	# then systems with lowest number of answers in priority.

	# Get system IDs
	connection.execute('select id_system, sum(nb_processed) as nb_answers from sample group by id_system order by __id__ asc')
	ids = connection.fetchall()
	# Keep fixed systems aside
	fixed_ids = []
	if nbFixed > 0:
		fixed_ids = ids[0:nbFixed]
		ids = ids[nbFixed:]
	# Sort remaining IDs according to number of answers
	ids = sorted(ids, key=lambda line: int(line[1]))
	# Let m the minimum number of answers
	# Shuffle all systems with number of answers ranging between m and m+delta
	m = ids[0][1]
	delta = 1
	low_votes_ids = list(filter(lambda line: line[1] <= m+delta, ids))
	random.shuffle(low_votes_ids)
	# And append others
	higher_votes_ids = list(filter(lambda line: line[1] > m+delta, ids))
	# Shuffle all systems with similar number of answers
	def gather_similar_systems(l):
		it = itertools.groupby(l, operator.itemgetter(1))
		for key, subiter in it:
			yield list(subiter)
	shuffled_higher_votes_ids = []
	for group in gather_similar_systems(higher_votes_ids):
		random.shuffle(group)
		shuffled_higher_votes_ids += group

	return [line[0] for line in fixed_ids+low_votes_ids+shuffled_higher_votes_ids];

def get_test_sample(user) :
	random.seed()
	nbToKeep = int(config.nbSystemDisplayed)
	dir = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(os.path.join(dir,'data.db'))
	c = conn.cursor()
	c.execute('select sample_index, sum(nb_processed) from sample where type="test" group by sample_index')
	res= c.fetchall()
	validlist=[]
	min=0
	for r in res :
		# Check if user have already done it
		c.execute('select count(*) from answer where user="'+user+'" and sample_index='+str(r[0])+' and question_index=1')
		nb = c.fetchall()
		if nb[0][0] ==0:
			if validlist==[]:
				min = r[1]
			if r[1] < min :
				min = r[1]
				validlist=[r]
			elif r[1]==min:
				validlist.append(r)
	index = validlist[random.randint(0,len(validlist)-1)][0]
	samples=[]
	systems=[]

	n = get_nb_position_fixed()

	shuffled_ids = get_shuffled_list_of_system_ids(n, c)

	headers = get_headers()
	queryh = ''
	for i in range(len(headers)) :
		queryh = queryh+headers[i]
		if i<len(headers)-1 :
			queryh=queryh+', '
	c.execute('select nb_processed, id_system, '+ queryh +' from sample where sample_index='+str(index)+' order by nb_processed asc')
	systs = {}
	for s in c.fetchall():
		systs[s[1]] = s

	i=0
	while i<nbToKeep :
		systems.append(shuffled_ids[i])
		t=dict()
		headerIndex=0
		for j in range(2,len(systs[shuffled_ids[i]])):
			if headers[headerIndex] in get_media() :
				t[headers[headerIndex]] = get_prefix()+'/media/'+systs[shuffled_ids[i][0]][j]
			else :
				t[headers[headerIndex]] = systs[shuffled_ids[i][0]][j]
			headerIndex+=1
		samples.append(t)
		i=i+1

	if n<=0:
		r = random.random()
		random.shuffle(samples, lambda: r)
		random.shuffle(systems, lambda: r)
	elif n>=get_nb_system_display():
		pass
	else :
		sa1 = samples[0:n]
		sa2 = samples[n:]
		sy1 = systems[0:n]
		sy2 = systems[n:]
		r = random.random()
		random.shuffle(sa2, lambda: r)
		random.shuffle(sy2, lambda: r)
		sa1.extend(sa2)
		samples=sa1
		sy1.extend(sy2)
		systems=sy1

	conn.close()
	return (samples, systems, index)

def get_trans_sample(user):
	random.seed()
	nbToKeep = int(config.nbSystemDisplayed)
	dir = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(os.path.join(dir,'data.db'))
	c = conn.cursor()
	c.execute('select sample_index, sum(nb_processed) from sample where type="test" group by sample_index')
	res= c.fetchall()
	validlist=[]
	min=0
	for r in res :
		# Check if user have already done it
		c.execute('select count(*) from answer where user="'+user+'" and sample_index='+str(r[0])+' and question_index=2')
		nb = c.fetchall()
		if nb[0][0] ==0:
			if validlist==[]:
				min = r[1]
			if r[1] < min :
				min = r[1]
				validlist=[r]
			elif r[1]==min:
				validlist.append(r)
	index = validlist[random.randint(0,len(validlist)-1)][0]
	samples=[]
	systems=[]

	n = get_nb_position_fixed()
	
	shuffled_ids = get_shuffled_list_of_system_ids(n, c)

	headers = get_headers()
	queryh = ''
	for i in range(len(headers)):
		queryh = queryh+headers[i]
		if i<len(headers)-1:
			queryh=queryh+', '
	c.execute('select nb_processed, id_system, '+ queryh +' from sample where sample_index='+str(index)+' order by nb_processed asc')
	systs = {}
	for s in c.fetchall():
		systs[s[1]] = s

	i=0
	while i<nbToKeep :
		systems.append(shuffled_ids[i])
		t=dict()
		headerIndex=0
		for j in range(2,len(systs[shuffled_ids[i]])):
			if headers[headerIndex] in get_media():
				t[headers[headerIndex]] = get_prefix()+'/media/'+systs[shuffled_ids[i][0]][j]
			else:
				t[headers[headerIndex]] = systs[shuffled_ids[i][0]][j]
			headerIndex+=1
		samples.append(t)
		i=i+1

	if n<=0:
		r = random.random()
		random.shuffle(samples, lambda: r)
		random.shuffle(systems, lambda: r)
	elif n>=get_nb_system_display():
		pass
	else:
		sa1 = samples[0:n]
		sa2 = samples[n:]
		sy1 = systems[0:n]
		sy2 = systems[n:]
		r = random.random()
		random.shuffle(sa2, lambda: r)
		random.shuffle(sy2, lambda: r)
		sa1.extend(sa2)
		samples=sa1
		sy1.expend(sy2)
		systems=sy1

	conn.close()
	return (samples, systems, index)

def get_intro_sample(user) :
	random.seed()
	nbToKeep = int(config.nbSystemDisplayed)
	dir = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(os.path.join(dir,'data.db'))
	c = conn.cursor()
	c.execute('select sample_index from sample where type="intro" group by sample_index')
	res= c.fetchall()
	index= res[0][0]
	for r in res :
		c.execute('select count(*) from answer where user="'+user+'" and sample_index='+str(r[0]))
		nb = c.fetchall()
		if nb[0][0] ==0:
			index = r[0]
	samples=[]
	systems=[]

	n = get_nb_position_fixed()

	shuffled_ids = get_shuffled_list_of_system_ids(n, c)

	headers = get_headers()
	queryh = ''
	for i in range(len(headers)) :
		queryh = queryh+headers[i]
		if i<len(headers)-1 :
			queryh=queryh+', '
	c.execute('select nb_processed, id_system, '+ queryh +' from sample where sample_index='+str(index)+' order by nb_processed asc')
	systs = {}
	for s in c.fetchall():
		systs[s[1]] = s

	i=0
	while i<nbToKeep :
		systems.append(shuffled_ids[i])
		t=dict()
		headerIndex=0
		for j in range(2,len(systs[shuffled_ids[i]])):
			if headers[headerIndex] in get_media() :
				t[headers[headerIndex]] = get_prefix()+'/media/'+systs[shuffled_ids[i][0]][j]
			else :
				t[headers[headerIndex]] = systs[shuffled_ids[i][0]][j]
			headerIndex+=1
		samples.append(t)
		i=i+1

	if n<=0:
		r = random.random()
		random.shuffle(samples, lambda: r)
		random.shuffle(systems, lambda: r)
	elif n>=get_nb_system_display():
		pass
	else :
		sa1 = samples[0:n]
		sa2 = samples[n:]
		sy1 = systems[0:n]
		sy2 = systems[n:]
		r = random.random()
		random.shuffle(sa2, lambda: r)
		random.shuffle(sy2, lambda: r)
		sa1.extend(sa2)
		samples=sa1
		sy1.extend(sy2)
		systems=sy1
	conn.close()
	return (samples, systems, index)

def insert_data(data) :
	now = datetime.now()
	conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.db'))
	c = conn.cursor()

	c.execute('select * from answer where user="'+str(data['user'])+'" and sample_index="'+str(data['sample_index'])+'" and question_index="1"')
	res = c.fetchall()
	c.execute('select * from answer where user="'+str(data['user'])+'" and sample_index="'+str(data['samp_index'])+'" and question_index="2"')
	res = res + c.fetchall()
	if len(res) == 0: # Check if the response is not already in the database

		sysval=''
		systs=''
		for i in range(int(config.nbSystemDisplayed)):
			sysval=sysval+'"'+data['systems'][i]+'"'
			systs=systs+'system'+str(i+1)
			if(i<int(config.nbSystemDisplayed)-1):
				sysval=sysval+','
				systs=systs+','
		# Update the number of time processed for the samples
		for sy in data['systems'] :
			c.execute('select nb_processed from sample where id_system="'+sy+'" and sample_index='+str(data['sample_index']))
			n = c.fetchall()[0][0]
			c.execute('update sample set nb_processed='+str(n+1)+' where id_system="'+sy+'" and sample_index='+str(data['sample_index']))
		conn.commit()
		answers = data['answers']
		for answer in answers :
			if answer['question_index'] == 1:
				val = '"'+str(data['user'])+'","'+str(now)+'","'+answer['content']+'","'+str(data['sample_index'])+'","'+str(answer['question_index'])+'","'+answer['system_index']+'",'+sysval
			else:
				content = answer['content'].replace('"',"'")
				val = '"'+str(data['user'])+'","'+str(now)+'","'+content+'","'+str(data['samp_index'])+'","'+str(answer['question_index'])+'","'+answer['sys_index']+'",'+sysval
			c.execute("insert into answer(user,date,content,sample_index,question_index,system_index,"+systs+") values ("+val+")")
		conn.commit()
"""
