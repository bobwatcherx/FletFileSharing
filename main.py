from flet import *
from appserver import MyStartServer,MyStopingserver
from appclient import ClientSend

def main(page:Page):


	# AND SWITCH FOR CHANGE IF YOU SERVER OR CLIENT
	def changejob(e):
		value = e.control.value
		print(" YOU selected is ",value)
		conServer.visible = True if value == True else False
		page.update()

		conClient.visible = True if value == False else False
		page.update()

	# CREATE SWITCH
	whoyou = Switch(
		label="you server",
		value=False,
		active_color="blue",
		on_change=changejob
	)


	def StartingServer(e):
		# FOR STARTTING SOCKET SERVER 
		# AND SHOW SNACKBAR
		page.snack_bar = SnackBar(
			Text("You server started",size=30),
			bgcolor="blue"
			)
		page.snack_bar.open = True
		# AND SHOW CONTAINER SERVER AND HIDE CLIENT CONTAINER
		btnStart.visible = False
		btnStop.visible = True
		page.update()
		MyStartServer()



	def StopingServer(e):
		page.snack_bar = SnackBar(
			Text("SOPPING SERVER",size=30),
			bgcolor="red"
			)
		page.snack_bar.open = True
		# AND SHOW CONTAINER SERVER AND HIDE CLIENT CONTAINER
		btnStart.visible = True
		btnStop.visible = False
		page.update()
		MyStopingserver()

	# CREATE BUTTON FOR START THE SERVER
	btnStart = ElevatedButton("Start YOu server",
		on_click=StartingServer
		)
	btnStop = ElevatedButton("Stopping server",
		on_click=StopingServer
		)

	# CREATE CONTAINER SERVER IF YOU SERVER
	conServer = Container(
		bgcolor="yellow200",
		padding=10,
		content=Column([
			Text("You is Server",size=30),
			Text("waiting from client send file",size=20),
			btnStart,
			btnStop

			])

		)

	# FOR ULOADING YOU FILE TO SERVER
	def uploadnow(e):
		# FOR SHOW YOU LOCATION FILE like /home/dd/file.Text
		for x in e.files:
			youfile = x.path
			ClientSend(youfile)

		page.update()

	# CREATE PICK FILE FOR UPLOAD

	file_picker = FilePicker(
		on_result=uploadnow

		)
	page.overlay.append(file_picker)


	# CREATE CLIENT CONTAINER IF YOU CLIENT
	conClient = Container(
		bgcolor="blue200",
		padding=10,
		content=Column([
			Text("You is Client",size=30),
			Text("Send file to server"),
			ElevatedButton("Upload file",
				bgcolor="white",color="black",
				on_click=lambda e:file_picker.pick_files()

			)
			])

		)

	# SET HIDE FOR DEFAULT WHEN YOU FLET IS OPEN 
	conServer.visible = False
	btnStop.visible = False

	page.add(
	Column([
	Text("File Sharing ",size=30,weight="bold"),
	whoyou,
	conClient,
	conServer

	])

	)
	
flet.app(target=main)