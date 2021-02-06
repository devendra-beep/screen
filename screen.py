
#author::devendra

import os
import shutil

l1="*" * 100
l2="-" * 100
print(l1)
print(l1)
print(l2)
print(l2)
print("                        ######    ######  #####  ######  #####  ##     #              ")
print("                        #         #       #  #   #       #      #  #   #              ")
print("                        ######    #       ###    ######  #####  #   #  #              ")
print("                             #    #       #  #   #       #      #    # #              ")
print("                        ######    ######  #   #  ######  #####  #     ##              ")
print("                                                                                      ")
print(l2)
print(l2)
print(l1)
print(l1)
print("\n")



print("Folder having Log Files")
log_f = input()
log_f=log_f.strip()

print("Approx Molecules")
ml=input()
mol=ml.strip()

print("Prefix")
prefx=input()
prefix=prefx.strip()

print("Suffix")
suffx=input()
suffix=suffx.strip()

pro_f="Output"

pro_f=pro_f.strip()

print("Name of output folder")
text_f=input()
text_f=text_f.strip()
os.mkdir(text_f)


while(True):
    print("\n")
    print("Press 0/1/2/3 -> Exit/Binding_Energy/Copy_pdbqt_for_given_binding_energy/Binding_Energy_of_All")
    #print("\n")
    nu=input("Choose::")
    nu=nu.strip()
    n=int(nu)
    if(n==0):
        break
    elif(n==1):
        name="Binding.txt"
        out = open(name, "w")
        print("Binding Energy Value")
        e_value=input()
        e_value=str(e_value.strip())
        value=float(e_value)
        l = len(mol)
        d1=log_f+prefix
        no_of_mol = int(mol)
        for i in range(1,no_of_mol):
            ll = l - len(str(i))
            s = ""
            s = ll * "0"
            st = s + str(i)
            d2=""
            d2 = d1+st+suffix
            if(os.path.isfile(d2)):
                new_f=open(d2)
                liness=new_f.readlines()
                xx=0
                for line in liness:
                    xx=xx+1
                    if(xx==28):
                        h = list(line.split())
                        vv = h[1]
                        vvv = float(vv)
                        if(vvv < value):
                            out.write("B-Energy in Ligand "+str(i)+" -> "+vv)
                            out.write("\n")
                new_f.close()
        out.close()
        print("Done")
        #shutil.copy(name, text_f)
    elif(n==2):
        list_values=[]
        print("Binding Energy Value")
        e_val=input()
        e_value=str(e_val)
        val=float(e_value)
        lm = len(mol)
        combine=log_f+prefix
        no_ = int(mol)
        for tt in range(1,no_):
            lll = lm - len(str(tt))
            tart = lll * "0"
            s = tart + str(tt)
            d_new = combine + s + suffix
            if(os.path.isfile(d_new)==True):
                file_ = open(d_new,"r")
                lines=file_.readlines()
                jj=0
                for line in lines:
                    jj=jj+1
                    if(jj==28):
                        water=list(line.split())
                        v=water[1]
                        g=float(v)
                        if(g<val):
                            list_values.append(tt)
                file_.close()
        pdb=".pdbqt.pdbqt"
        for kk in (list_values):
            var = lm - len(str(kk))
            shortv = var * "0"
            ss = shortv + str(kk)
            rock = log_f+prefix+ss+pdb
            if(os.path.isfile(rock)):
                shutil.copy(rock, text_f)
        print("Done")
    elif(n==3):
        names="All.txt"
        o = open(names, "w")
        l = len(mol)
        no_of_mol = int(mol)
        for i in range(1,no_of_mol):
            ll = l - len(str(i))
            s = ll * "0"
            s = s + str(i)
            d6 = log_f+prefix+s+suffix
            if(os.path.isfile(d6)==True):
                fi = open(d6,"r")
                lines = fi.readlines()
                jj=0
                for line in lines:
                    jj=jj+1
                    if(jj==28):
                        z=list(line.split())
                        v=z[1]
                        state="Energy of ligand "+str(i)+" -> "+v
                        o.write(state)
                        o.write("\n")
                fi.close()
        o.close()
        print("Done")
        #shutil.copy(names, text_f)

print("Over")
