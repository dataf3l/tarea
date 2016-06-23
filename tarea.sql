select 
	location,
		(((acos(sin(('[#lat]'*pi()/180)) * sin((city.latitude*pi()/180))+cos(('[#lat]'*pi()/180)) * cos((city.latitude*pi()/180)) * 
		cos((('[#lon]'- city.longitude)*pi()/180))))*180/pi())*60*1.1515) 
			AS distance,
			city.latitude,
			city.longitude
		from 
			city
		order by id
