#file = open("xFile.txt","w")
# file = open ("C:/Klasör/xFile.txt","w")
#file.close()
# Open File and write with encoding
#file = open("xFile1.txt","w",encoding = 'utf-8')
#file.write("Python Programming")
#file.close()

#Append
#file = open("xFile1.txt","a",encoding = 'utf-8')
#file.write("\nGo Programming")
#file.close()
#
# Create - If file exists , it will get error. Else create file
#file = open("xFile2.txt","x",encoding = 'utf-8')
#file.write("Go Programming")
#file.close()

# Read File
#x = open("xxxx.txt","r")



try:
    f = open("xFile.txt",'r')
    try:
        data = f.Read()
        print(data)
    except IOError as e:
        print(e)
    except ValueError as e:
        print(e)
    except EOFError as e:
        print(e)
    except: #Other exceptions
        print(e)
    finally:
        f.close()
except:
    print("We got error")
finally:
    print("All done")