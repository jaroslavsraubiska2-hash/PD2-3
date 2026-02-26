# Username; Role; DaysSincePWChange; LastLogin(h)
users = [
"admin_jv;Administrator;5;1",
"karlis_o;User;120;48",
"anna_l;Manager;45;10",
"guest_01;Guest;1;0",
"root;SuperUser;350;5",
"audit_user;Auditor;10;170",
"test_account;Guest;95;200",
"support_v;Administrator;85;2",
"operator_1;User;30;20",
"aguest_new;Guest;2;1"
]

privileged =[]

for u in users:
    parts = u.split(";")
    username = parts[0]
    role = parts[1]
    
    if role in ["Administrator","SuperUser"]:
        privileged.append (username)
        
    print("Prevelģeto kontu skaits:", len (privileged))
    for p in privileged:
        print(p)