# Day 6: Vectors for Machine Learning
# representing vectors  as Lists 
vector_a = [1,2,3]
vector_b = [4,5,6]
print("Vector A:", vector_a)
print("Vector B:", vector_b)

# Vector Addition
vector_sum=[]
for i  in range(len(vector_a)):
    vector_sum.append(vector_a[i] + vector_b[i])
print("Vector Addition:", vector_sum)

#  Dot product
vector_dotproduct=[]
for i in range(len(vector_a)):
    vector_dotproduct.append(vector_a[i] *  vector_b[i])
print(" Dot product:",vector_dotproduct)

