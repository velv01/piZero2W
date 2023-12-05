A = [[5,2,3],
    [2 ,1,3],
    [2 ,4,3]]

B = [[2,2,1,2],
    [3,2,3,0],
    [0,2,4,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(A)):
   for j in range(len(B[0])):
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

for i in range(3):
  for j in range(4):
     print(result[i][j], end="")
     print(" ", end="")
  print("\n")
 




   


   
   




 



    

    
    

