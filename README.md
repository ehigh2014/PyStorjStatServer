Project Name: PyStorjStatServer
=====================================================
The server for handling the clients status info.
=====================================================

# Components
## redis server
	sudo apt-get install redis-server
	pip install redis

## flask and flask_table
  <code>pip install flask</code><br>
  <code>pip install flask_table</code>

## daemon (run in background)
	<code>pip install python-deamon</code>
  
# Run Server 
	python main.py
	nohup python main.py & (run in background)