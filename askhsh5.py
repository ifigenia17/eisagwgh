for i in range (1,1001):
	if i>=1 and i<=9:
	  print "O arithmos",i,"einai Harshad"
	elif i>=10 and i<=99:
		x1=i/10
		x2=i%10
		if i%(x1+x2)==0:
			print "O arithmos",i,"einai Harshad"
		if x1*x2!=0:
			if i%(x1*x2)==0:
				print "O arithmos",i,"diareitai apo to ginomeno twn pshfiwn tou"
	elif i>=100 and i <=999:
		x1=i/100
		x2=(i%100)/10
		x3=i%10
		if i%(x1+x2+x3)==0:
		  print "O arithmos",i,"einai Harshad"
		  if (x1*x2*x3)!=0:
		    if i%(x1*x2*x3)==0:
		      print "O arithmos",i,"diareitai apo to ginomeno twn pshfiwn tou"
	else: 
	  print "O arithmos",i,"einai Harshad"