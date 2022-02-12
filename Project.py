import os
os.system('cls')
patient_file = open("patients.txt","a")
patient_file.close()
doctor_file = open("doctors.txt","a")
doctor_file.close()
appoint_file = open("appointments.txt","a")
appoint_file.close()


admin_flag =0
user_flag=0
prog_flag =1
i=0



while prog_flag==1:
	
	print("|***********************************************|")
	print("|           Hospital Management system          |")
	print("|***********************************************|")
	print("| 1- To Enter Admin Mode Press 1                |")
	print("| 2- To Enter User Mode Press 2                 |")
	print("| 3- To Exit From Program Press 3               |")
	print("|***********************************************|")
	choice = input(" Please enter your choice ( 1 or 2 ): ")

	if str(choice) == "1":
		os.system('cls')
		print("|-------------------------------------------|")
		i=3
		while (i > 0) and (admin_flag==0):
			password = str(input(" Please enter your Password: "))
			if password == "1234":
				admin_flag =1
			else:
				print(" Wrong Password\n")
				i = i -1
		if(i==0):
			print(" Wrong Password for 3 times\n")
			prog_flag=0
		print("|-------------------------------------------|")
	
	elif str(choice) == "2":
		os.system('cls')
		user_flag = 1
		
	elif str(choice) == "3":
		prog_flag=0
	else:
		print(" Invalid Choice")


	while admin_flag ==1:

		print("|***********************************************|")
		print("|                Admin Mode                     |")
		print("|***********************************************|")
		print("| 1- To Manage Patients Press 1                 |")
		print("| 2- To Manage Doctors Press 2                  |")
		print("| 3- To Book An Appointment Press 3             |")
		print("| 4- To Exit Admin Mode Press 4                            |")
		print("|***********************************************|")
		choice = str(input(" Please enter your choice ( 1 - 2 - 3 - 4 ):  "))
		
	#*************************************    Patients Section *************************************
		if choice == "1":
			os.system('cls')
			print("|-----------------------------------------------|")
			print("| 1- To Add Patient Press 1                     |")
			print("| 2- To Edit Patient Press 2                    |")
			print("| 3- To Delete Patient Press 3                  |")
			print("| 4- To Display Patient Press 4                 |")
			print("| 5- To Display All Patients Press 5            |")			
			print("|-----------------------------------------------|")
			choice = str(input(" Please enter your choice ( 1 - 2 - 3 - 4 - 5 ):  "))
			
			# ###########################################   Add  ######################################
			if choice =="1":
				os.system('cls')
				ID = str(input("Please Enter ID of Patient To Add (in Digits) : "))
				patient_file = open("patients.txt","r")
				data = patient_file.read()
				
				if (("ID : "+str(ID)) in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Already Exist ")
				elif ID.isdigit(): 
					department = str(input("Please Enter The Department : "))
					doctor     = str(input("Please Enter Name of the Doctor : "))
					name       = str(input("Please Enter Name of Patient : "))
					age        = str(input("Please Enter The Age of Patient : "))
					gender     = str(input("Please Enter Gender of Patient : "))
					address    = str(input("Please Enter Address of Patient : "))
					phone      = str(input("Please Enter Phone Number of Patient : "))
					room       = str(input("Please Enter Room Number of Patient : "))
					condition  = str(input("Please Describe the patient's condition : "))
		
					patient_file = open("patients.txt","a")
					patient_file.write("["+"\n")
					patient_file.write("ID : "+str(ID)+"\n")
					patient_file.write("Department : "+str(department)+"\n")
					patient_file.write("Doctor Name : "+str(doctor)+"\n")
					patient_file.write("Patient Name : "+name+"\n")
					patient_file.write("Age : "+age+"\n")
					patient_file.write("Gender : "+gender+"\n")
					patient_file.write("Address : "+address+"\n")
					patient_file.write("Phone Number : "+phone+"\n")
					patient_file.write("Room Number : "+room+"\n")
					patient_file.write("Condition : "+condition+"\n")
					patient_file.write("]"+"\n")
					patient_file.close()
					print("|-----------------------------------------------|")
					print(" Added Successfully, Thank You")
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Edit   ######################################
			elif choice =="2":
				os.system('cls')
				ID = str(input("Please Enter ID of Patient To Edit (in Digits) : "))
				patient_file = open("patients.txt","r")
				data = patient_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					department = str(input("Please Enter The Department : "))
					doctor     = str(input("Please Enter Name of the Doctor : "))
					name       = str(input("Please Enter Name of Patient : "))
					age        = str(input("Please Enter The Age of Patient : "))
					gender     = str(input("Please Enter Gender of Patient : "))
					address    = str(input("Please Enter Address of Patient : "))
					phone      = str(input("Please Enter Phone Number of Patient : "))
					room       = str(input("Please Enter Room Number of Patient : "))
					condition  = str(input("Please Describe the patient's condition : "))
					patient_file = open("patients.txt","r")
					data = patient_file.readlines()
					patient_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							index = data.index(line)
							data[index+1] ="Department : "+str(department)+"\n"
							data[index+2] ="Doctor Name : "+str(doctor)+"\n"
							data[index+3] ="Patient Name : "+name+"\n"
							data[index+4] ="Age : "+age+"\n"
							data[index+5] ="Gender : "+gender+"\n"
							data[index+6] ="Address : "+address+"\n"
							data[index+7] ="Phone Number : "+phone+"\n"
							data[index+8] ="Room Number : "+room+"\n"
							data[index+9] ="Condition : "+condition+"\n"
							patient_file = open("patients.txt","w")
							for new_line in data:
								patient_file.write(new_line)
							patient_file.close()
							print("----------------------------------------------------")
							print (" Edited Successfully ")
							break
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Delete   ######################################
			elif choice =="3":
				os.system('cls')
				ID = str(input("Please Enter ID of Patient To Delete (in Digits) : "))
				patient_file = open("patients.txt","r")
				data = patient_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					patient_file = open("patients.txt","r")
					data = patient_file.readlines()
					patient_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							index = data.index(line)
							data[index-1] =''
							data[index] =''
							data[index+1] =''
							data[index+2] =''
							data[index+3] =''
							data[index+4] =''
							data[index+5] =''
							data[index+6] =''
							data[index+7] =''
							data[index+8] =''
							data[index+9] =''
							data[index+10] =''
							patient_file = open("patients.txt","w")
							for new_line in data:
								patient_file.write(new_line)
							patient_file.close()
							print("----------------------------------------------------")
							print(" Deleted Successfully ")
							break	
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Display One   ######################################
			elif choice =="4":
				os.system('cls')
				ID = str(input("Please Enter ID of Patient To Display (in Digits) : "))
				patient_file = open("patients.txt","r")
				data = patient_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					patient_file = open("patients.txt","r")
					data = patient_file.readlines()
					patient_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							
							index = data.index(line)
							print(data[index])
							print(data[index+1])
							print(data[index+2])
							print(data[index+3])
							print(data[index+4])
							print(data[index+5])
							print(data[index+6])
							print(data[index+7])
							print(data[index+8])
							print(data[index+9])
							break	
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Display All   ######################################
			elif choice =="5":
				os.system('cls')
				patient_file = open("patients.txt","r")
				data = patient_file.readlines()
				patient_file.close()
				for line in data:
					if ("ID : ") == line[:line.find("\n")-1]:
						index = data.index(line)
						print("------------------------------------------------")
						print(data[index])
						print(data[index+1])
						print(data[index+2])
						print(data[index+3])
						print(data[index+4])
						print(data[index+5])
						print(data[index+6])
						print(data[index+7])
						print(data[index+8])
						print(data[index+9]) 
						print("-------------------------------------------------")
			else:
				os.system('cls')
				print("----------------------------------------------------")
				print(" Invalid Choice ")
			
	#*********************************    Doctors Section ****************************************************
	
		elif choice =="2":
			os.system('cls')
			print("|-----------------------------------------------|")
			print("| 1- To Add Doctor Press 1                      |")
			print("| 2- To Edit Doctor Press 2                     |")
			print("| 3- To Delete Doctor Press 3                   |")
			print("| 4- To Display Doctor Press 4                  |")	
			print("| 5- To Display All Doctor Press 5              |")			
			print("|-----------------------------------------------|")
			choice = str(input(" Please enter your choice ( 1 - 2 - 3 - 4 - 5 ):  "))
			
			# ###########################################   Add   ######################################
			if choice =="1":
				os.system('cls')
				ID = str(input("Please Enter ID of Doctor To ADD (in Digits) : "))
				doctor_file = open("doctors.txt","r")
				data = doctor_file.read()
				
				if (("ID : "+str(ID)) in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Already Exist ")
				elif ID.isdigit(): 
					department = str(input("Please Enter The Department : "))
					doctor     = str(input("Please Enter Name of the Doctor : "))
					address    = str(input("Please Enter Address of Doctor : "))
					phone      = str(input("Please Enter Phone Number of Doctor : "))
		
					doctor_file = open("doctors.txt","a")
					doctor_file.write("["+"\n")
					doctor_file.write("ID : "+str(ID)+"\n")
					doctor_file.write("Department : "+str(department)+"\n")
					doctor_file.write("Doctor Name : "+str(doctor)+"\n")
					doctor_file.write("Phone Number : "+phone+"\n")
					doctor_file.write("Address : "+address+"\n")
					doctor_file.write("]"+"\n")
					doctor_file.close()
					print("|-----------------------------------------------|")
					print(" Added Successfully, Thank You")
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Edit   ######################################
			elif choice =="2":
				os.system('cls')
				ID = str(input(" Please Enter ID of Doctor to Edit (in Digits) : "))
				doctor_file = open("doctors.txt","r")
				data = doctor_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					department = str(input("Please Enter The Department : "))
					doctor     = str(input("Please Enter Name of the Doctor : "))
					address    = str(input("Please Enter Address of Doctor : "))
					phone      = str(input("Please Enter Phone Number of Doctor : "))
					doctor_file = open("doctors.txt","r")
					data = doctor_file.readlines()
					doctor_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							index = data.index(line)
							data[index+1] ="Department : "+str(department)+"\n"
							data[index+2] ="Doctor Name : "+str(doctor)+"\n"
							data[index+3] ="Address : "+address+"\n"
							data[index+4] ="Phone Number : "+phone+"\n"
							doctor_file = open("doctors.txt","w")
							for new_line in data:
								doctor_file.write(new_line)
							doctor_file.close()
							print("----------------------------------------------------")
							print (" Edited Successfully ")
							break
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Delete   ######################################
			elif choice =="3":
				os.system('cls')
				ID = str(input(" Please Enter ID of Doctor to Delete (in Digits) : "))
				doctor_file = open("doctors.txt","r")
				data = doctor_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					doctor_file = open("doctors.txt","r")
					data = doctor_file.readlines()
					doctor_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							index = data.index(line)
							data[index-1] =''
							data[index] =''
							data[index+1] =''
							data[index+2] =''
							data[index+3] =''
							data[index+4] =''
							data[index+5] =''
							doctor_file = open("doctors.txt","w")
							for new_line in data:
								doctor_file.write(new_line)
							doctor_file.close()
							print("----------------------------------------------------")
							print(" Deleted Successfully ")
							break
				else:
					os.system('cls')
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
					print("|-----------------------------------------------|")
			# ###########################################   Display One   ######################################
			elif choice =="4":
				os.system('cls')
				print("|-----------------------------------------------|")
				ID = str(input(" Please Enter ID of The Doctor (in Digits) : "))
				doctor_file = open("doctors.txt","r")
				data = doctor_file.read()
				
				if (("ID : "+str(ID)) not in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" ID Doesn't Exist ")
				elif ID.isdigit(): 
					doctor_file = open("doctors.txt","r")
					data = doctor_file.readlines()
					doctor_file.close()
					index= 0;
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							
							index = data.index(line)
							print(data[index])
							print(data[index+1])
							print(data[index+2])
							print(data[index+3])
							print(data[index+4])
							break
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# ###########################################   Display All   ######################################
			elif choice =="5":
				os.system('cls')
				doctor_file = open("doctors.txt","r")
				data = doctor_file.readlines()
				doctor_file.close()
				for line in data:
					if ("ID : ") == line[:line.find("\n")-1]:
						index = data.index(line)
						print("------------------------------------------------")
						print(data[index])
						print(data[index+1])
						print(data[index+2])
						print(data[index+3])
						print(data[index+4])
						print("-------------------------------------------------")
			else:
				os.system('cls')
				print("----------------------------------------------------")
				print(" Invalid Choice ")
				print("----------------------------------------------------")
			
	#*******************************************    Appointments Section *****************************************************

		elif choice =="3":
			os.system('cls')
			print("|-----------------------------------------------|")
			print("| 1- To Book An Appointment Press 1             |")
			print("| 2- To Edit An Appointment Press 2             |")
			print("| 3- To Cancel An Appointment Press 3           |")
			print("|-----------------------------------------------|")		
			choice = str(input(" Please enter your choice ( 1 - 2 - 3 ):  "))
			
			# #####################################   Book  ######################################
			if choice =="1":
				
				ID = str(input("Please Enter ID of Patient To Add Booking (in Digits) : "))
				appoint_file = open("appointments.txt","r")
				data = appoint_file.read()
				
				if (("ID : "+str(ID)) in data) and ID.isdigit():
					print("----------------------------------------------------")
					print(" Patient ID Already Exist in Booking System")
				elif ID.isdigit(): 
					doctor_ID  = str(input("Please Enter ID of the Doctor : "))
					doctor_file = open("doctors.txt","r")
					data = doctor_file.read()
					if (("ID : "+str(doctor_ID)) in data) and doctor_ID.isdigit():
					
						doctor_file = open("doctors.txt","r")
						data = doctor_file.readlines()
						for line in data:
							if ("ID : "+str(doctor_ID)) == line[:line.find("\n")]:
								index = data.index(line)
								doctor = data[index+2]
								break
							
						time       = str(input("Please Enter The Time of Appointment : "))
						appoint_file = open("appointments.txt","r")
						data = appoint_file.read()
						if (("Time : "+str(time)) not in data) and time.isdigit() :
							if (int(time) > 0) and (int(time) < 24):
								department = str(input("Please Enter The Department : "))
								name       = str(input("Please Enter Name of the Patient : "))
								age        = str(input("Please Enter Age of the Patient : "))
								gender     = str(input("Please Enter Gender of the Patient : "))
		
								appoint_file = open("appointments.txt","a")
								appoint_file.write("["+"\n")
								appoint_file.write("ID : "+str(ID)+"\n")
								appoint_file.write("Department : "+str(department)+"\n")
								appoint_file.write("Doctor ID : "+str(doctor_ID)+"\n")
								appoint_file.write(doctor)
								appoint_file.write("Patient Name : "+name+"\n")
								appoint_file.write("Patient Age : "+age+"\n")
								appoint_file.write("Patient Gender : "+gender+"\n")
								appoint_file.write("Time : "+time+"\n")
								appoint_file.write("]"+"\n")
								appoint_file.close()
								print("|-----------------------------------------------|")
								print(" Booked Successfully, Thank You")
							else:
								print("|-----------------------------------------------|")
								print(" Time Must Be In Numbers Between (0 - 23)")
						elif time.isdigit():
							print("----------------------------------------------------")
							print(" This Appointment time is Reserved ")
						else:
							print("|-----------------------------------------------|")
							print(" Time Must Be In Numbers Between (0 - 23) Only ")
							
					elif doctor_ID.isdigit() :
						print("----------------------------------------------------")
						print(" Doctor ID doesn't exist ")
					else:
						print("----------------------------------------------------")
						print(" Doctor ID Must Be Number ")
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
			# #####################################   Edit  ######################################
			elif choice =="2":
				ID = str(input("Please Enter ID of Patient To Edit Booing (in Digits) : "))
				appoint_file = open("appointments.txt","r")
				data = appoint_file.read()
				
				if (("ID : "+str(ID)) in data) and ID.isdigit():
				
					doctor_ID  = str(input("Please Enter New ID of the Doctor : "))
					doctor_file = open("doctors.txt","r")
					data = doctor_file.read()
					if (("ID : "+str(doctor_ID)) in data) and doctor_ID.isdigit():
						doctor_file = open("doctors.txt","r")
						data = doctor_file.readlines()
						for line in data:
							if ("ID : "+str(doctor_ID)) == line[:line.find("\n")]:
								index = data.index(line)
								doctor = data[index+2]
								break
							
						time = str(input("Please Enter The New Time of Appointment : "))
						appoint_file = open("appointments.txt","r")
						data = appoint_file.read()
						if (("Time : "+str(time)) not in data) and time.isdigit() :
							if (int(time) > 0) and (int(time) < 24):
								department = str(input("Please Enter The New Department : "))
								name       = str(input("Please Enter New Name of the Patient : "))
								age        = str(input("Please Enter New Age of the Patient : "))
								gender     = str(input("Please Enter New Gender of the Patient : "))
								
								appoint_file = open("appointments.txt","r")
								data = appoint_file.readlines()
								for line in data:
									if ("ID : "+str(ID)) == line[:line.find("\n")]:
										index = data.index(line)
										data[index+1] ="Department : "+str(department)+"\n"
										data[index+2] ="Doctor ID : "+str(doctor_ID)+"\n"
										data[index+3] = doctor
										data[index+4] = "Patient Name : "+name+"\n"
										data[index+5] = "Patient Age : "+age+"\n"
										data[index+6] = "Patient Gender : "+gender+"\n"
										data[index+7] = "Time : "+time+"\n"
										appoint_file = open("appointments.txt","w")
										for new_line in data:
											appoint_file.write(new_line)
										appoint_file.close()
										print("----------------------------------------------------")
										print (" Edited Successfully, Thank You ")
										break
							else:
								print("|-----------------------------------------------|")
								print(" Time Must Be In Numbers Between (0 - 23)")
						elif time.isdigit():
							print("----------------------------------------------------")
							print(" This Appointment time is Reserved ")
						else:
							print("|-----------------------------------------------|")
							print(" Time Must Be In Numbers Between (0 - 23) Only ")
							
					elif doctor_ID.isdigit() :
						print("----------------------------------------------------")
						print(" Doctor ID doesn't exist ")
					else:
						print("----------------------------------------------------")
						print(" Doctor ID Must Be Number ")		
				elif ID.isdigit(): 
					print("----------------------------------------------------")
					print(" Patient ID Doesn't Exist in Booking System")
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")

			# #####################################   Delete  ######################################
			elif choice =="3":
			
				ID = str(input("Please Enter ID of Patient To Remove Booing (in Digits) : "))
				appoint_file = open("appointments.txt","r")
				data = appoint_file.read()
				
				if (("ID : "+str(ID)) in data) and ID.isdigit():
								
					appoint_file = open("appointments.txt","r")
					data = appoint_file.readlines()
					for line in data:
						if ("ID : "+str(ID)) == line[:line.find("\n")]:
							index = data.index(line)
							data[index-1] =''
							data[index]   =''
							data[index+1] =''
							data[index+2] =''
							data[index+3] = ''
							data[index+4] = ''
							data[index+5] = ''
							data[index+6] = ''
							data[index+7] = ''
							data[index+8] =''
							appoint_file = open("appointments.txt","w")
							for new_line in data:
								appoint_file.write(new_line)
							appoint_file.close()
							print("----------------------------------------------------")
							print (" Removed Successfully, Thank You ")
							break
				elif ID.isdigit(): 
					print("----------------------------------------------------")
					print(" Patient ID Doesn't Exist in Booking System")
				else:
					print("|-----------------------------------------------|")
					print(" ID Must Be In Numbers")
	
		elif choice =="4":
			admin_flag=0
			os.system('cls')
		
		else:
			os.system('cls')
			print("Invalid Choice")
		
	#*******************************************    User Mode *****************************************************
	while user_flag==1:
		print("|***********************************************|")
		print("|                User Mode                      |")
		print("|***********************************************|")
		print("| 1- To View all departments Press 1            |")
		print("| 2- To View all doctors Press 2                |")
		print("| 3- To View all patients Press 3               |")
		print("| 4- To View patient Details Press 4            |")
		print("| 5- To View Doctor Appointment Press 5         |")
		print("| 6- To Exit User Mode Press 6                  |")
		print("|***********************************************|")
		choice = str(input(" Please enter your choice ( 1-2-3-4-5 ):  "))		
		
		if str(choice) == "1":
			os.system('cls')
			print ("ALL Departments are : ")
			print ("1- Cardiology ")
			print ("2- Intensive Care Unit (ICU)")
			print ("3- Surgery")
			print ("4- Burn Center")
			print ("5- Pharmacy")
			
		elif str(choice) == "2":
			os.system('cls')
			doctor_file = open("doctors.txt","r")
			data = doctor_file.readlines()
			doctor_file.close()
			for line in data:
				if ("ID : ") == line[:line.find("\n")-1]:
					index = data.index(line)
					print("------------------------------------------------")
					print(data[index])
					print(data[index+1])
					print(data[index+2])
					print(data[index+3])
					print(data[index+4])
					print("-------------------------------------------------")
			
		elif str(choice) == "3":
			os.system('cls')	
			patient_file = open("patients.txt","r")
			data = patient_file.readlines()
			patient_file.close()
			for line in data:
				if ("ID : ") == line[:line.find("\n")-1]:
					index = data.index(line)
					print("------------------------------------------------")
					print(data[index])
					print(data[index+1])
					print(data[index+2])
					print(data[index+3])
					print(data[index+4])
					print(data[index+5])
					print(data[index+6])
					print(data[index+7])
					print(data[index+8])
					print(data[index+9]) 
					print("-------------------------------------------------")
					
					
		elif str(choice) == "4":
			os.system('cls')
			ID = str(input("Please Enter ID of Patient To Display (in Digits) : "))
			patient_file = open("patients.txt","r")
			data = patient_file.read()
				
			if (("ID : "+str(ID)) not in data) and ID.isdigit():
				print("----------------------------------------------------")
				print(" ID Doesn't Exist ")
			elif ID.isdigit(): 
				patient_file = open("patients.txt","r")
				data = patient_file.readlines()
				patient_file.close()
				index= 0;
				for line in data:
					if ("ID : "+str(ID)) == line[:line.find("\n")]:
							
						index = data.index(line)
						print(data[index])
						print(data[index+1])
						print(data[index+2])
						print(data[index+3])
						print(data[index+4])
						print(data[index+5])
						print(data[index+6])
						print(data[index+7])
						print(data[index+8])
						print(data[index+9])
						break	
			else:
				print("|-----------------------------------------------|")
				print(" ID Must Be In Numbers")
				
				
		elif str(choice) == "5":
			os.system('cls')
			ID = str(input("Please Enter ID of Doctor To Display Appointments(in Digits) : "))
			appoint_file = open("appointments.txt","r")
			data = appoint_file.read()
				
			if (("Doctor ID : "+str(ID)) not in data) and ID.isdigit():
				print("----------------------------------------------------")
				print(" ID Doesn't Exist ")
			elif ID.isdigit(): 
				appoint_file = open("appointments.txt","r")
				data = appoint_file.readlines()
				appoint_file.close()
				index= 0;
				for line in data:
					if ("Doctor ID : "+str(ID)) == line[:line.find("\n")]:
							
						index = data.index(line)
						print(data[index-2])
						print(data[index-1])
						print(data[index])
						print(data[index+1])
						print(data[index+2])
						print(data[index+3])
						print(data[index+4])
						print(data[index+5])
						break	
			else:
				print("|-----------------------------------------------|")
				print(" ID Must Be In Numbers")			
			
		elif str(choice) == "6":
			user_flag=0
			os.system('cls')
		else:
			os.system('cls')
			print("----------------------------------------------------")
			print(" Invalid Choice ")
			print("----------------------------------------------------")
		
		