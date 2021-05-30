def time_convert(var1="9:10 AM", var2=200):
    hours = var1.split()[0].split(":")[0]
    minutes = var1.split()[0].split(":")[1]
    am_or_pm = var1.split()[1]

    total_minutes = int(minutes) + var2
    print(total_minutes)
    if total_minutes >= 60:
        extra_hr = total_minutes//60
        remaining_minutes = total_minutes - 60*extra_hr
        new_hour = int(hours) + extra_hr
        print(new_hour, remaining_minutes)
        if new_hour >= 12:
            if am_or_pm == 'AM':
                am_or_pm = 'PM'
            else:
                am_or_pm = 'AM'

            if new_hour == 12:
                hours = new_hour
                return f"{hours}:{remaining_minutes} {am_or_pm}"
            else:
                hours = new_hour - 12
                return f"{hours}:{remaining_minutes} {am_or_pm}"
        else:
            return f"{new_hour}:{remaining_minutes} {am_or_pm}"


print(time_convert())
print(time_convert(var1="9:10 PM", var2=300))


"""
/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
		String str1 = "9:10 AM";
		String str2 = "200"
		String[] arr = str1.split(" ", 0);
		String time = arr[0];
		String am_or_pm = arr[1];
		System.out.println(time);
		System.out.println(am_or_pm);
		String[] time_data = time.split(":", 0);
		String hours = time_data[0];
		String minutes = time_data[1];
		
		System.out.println("hours :"+ hours);
		System.out.println("minutes :"+ minutes);
		
		Integer total_minutes = int(minutes) + int(str2);
		if (total_minutes >= 60)
		{
		    Integer exstra_hr = total_minutes/60;
		    Integer remain_minutes = total_minutes - 60*exstra_hr;
		    Integer hours = int(hours) + exstra_hr
		    if(hours >=12){
		        if(am_or_pm == 'AM'){
		            am_or_pm = 'PM';
		             }
		         else{
		             am_or_pm = 'AM'
		         }
		         
		         if(hours == 12){
		            return str(hours)+":"+remain_minutes+" "+am_or_pm 
		         }
		           hours = hours - 12
		           retun String(hours)+":"+String
		    }
		} 
		
	}
}


"""