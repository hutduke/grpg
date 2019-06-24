import jobs

print ("Welcome to the world!")
print ("Enter your name")
name = input()
print ("Welcome:", name)
job_selection = False
while job_selection == False:
    print ("Select a job")
    print (jobs.joblist)
    player_job = input()
    player_job = player_job.upper()
    for job in jobs.joblist:
        if player_job[0]== job[0].upper():
            player_job = job
            job_selection = True
        if player_job == job.upper():
            job_selection = True
    if job_selection == False:
        print ("Invalid input.")

#making an appropriate Object of the Job class
#open jobs.dat
#find the necessary Job that is ==player_job
#pjob = job(player_job)

print ("Behold! A new era is dawning on the continent!")
print ("The fresh hero", name + ", a mighty", player_job, "in the making")
print ("is beginning their adventure! What wonderous deeds they shall lay")
print ("a claim to, what legends their tale will give life!")

print ("View skills? (Y/N)")
answer = input()
if answer.upper() == "Y":
    for skill in pjob.skills:
        print (skill.description)
if answer.upper() == "N":
    print ("Okay!")

