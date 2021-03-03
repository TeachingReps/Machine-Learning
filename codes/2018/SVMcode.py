
#==============================================================================
#     Install "qpsolvers" package
#     Installation command for Linux users: pip install qpsolvers
#==============================================================================

import numpy as np
from qpsolvers import solve_qp



    
def SVM_learner(traindata, trainlabels, C):
    
#     INPUT : 
#     traindata   - m X n matrix, where m is the number of training points
#     trainlabels - m X 1 vector of training labels for the training data
#     C           - SVM regularization parameter (positive real number)
#     
#     
#     OUTPUT :
#     returns the structure 'model' which has the following fields:
#     
#     b - SVM bias term
#     sv - the subset of training data, which are the support vectors
#     sv_alphas - m X 1 vector of support vector coefficients
#     sv_labels - corresponding labels of the support vectors



#    Solve the SVM dual optimization problem using "qpsolvers" package.


#                        "qpsolvers" package guide

#       Wrapper around Quadratic Programming (QP) solvers in Python, with a 
#        unified interface.

#          Github link: https://github.com/stephane-caron/qpsolvers

             
#         Installation command for Linux users: pip install qpsolvers

#         A quadratic program (QP) is written in standard form as:
#         
#                   minimize (1/2) x^TPx + q^Tx
#                   subject to Gx <= h, Ax = u
#      
# 
#     Here, x is the vector of optimization variables. The matrix P and 
#     vector q are used to define any quadratic 
#     objective function on these variables, while the matrix-vector couples 
#    (G,h) and (A,u) respectively define inequality and equality constraints. 
#    Vector inequalities apply coordinate by coordinate.



#     Express P, q, G, h, A, u for the SVM dual optimization problem and then 
#     solve the dual variables. Example usage:
    
#                 alphas = solve_qp(P, q, G, h, A, u)

#      Useful tip: If you encounter the following error message 
#      "matrix G is not positive definite", add 1e-5 to the diagonal entries
#      of P to make it positive definite



#      Write code here to find b, support_vectors, support_vector_alphas and
#      support_vector_labels


    

    
            
        
    
    
#==============================================================================
    
    class model_struct:
        pass
    
    
    model = model_struct()
    model.b = b
    model.sv = support_vectors
    model.sv_alphas = support_vector_alphas
    model.sv_labels = support_vector_labels
    
    return model
    
    
def SVM_classifier(testdata, model):
    

#     INPUT
#     testdata - m X n matrix of the test data samples
#     # model    - SVM model structure returned by SVM_learner
#     
#     OUTPUT
#     predictedlabels - m x 1 vector of predicted labels
#     
#     Write code here to find predictedlabels


    
   
                           
#==============================================================================                           
        
    
    return predictedlabels
  


  
def classification_error(predictedlabels, testlabels):
    


#      This function computes the classification error for the predicted labels
#       with respect to the ground truth. The returned error value is a real 
#       number between 0 and 1 (fraction of misclassications).
# 
#   testlabels: vector of true labels (each label +1/-1)
#   predictedlabels: vector of predicted labels (each prediction +1/-1)
#   percentage_error: classification error (percentage of misclassifications)

#   You don't need to write anyhing here


    
    err = float(np.sum(predictedlabels != testlabels))
    percentage_error = err*100/len(testlabels)
    
    return percentage_error
    
    
    


#   Write main routine here. We should be able to run your code for any value
#   of C, training dataset and text dataset
        


C = your_C_value        # Put values of C here   

train = np.loadtxt('your_training_data.txt') # load training dataset here

test = np.loadtxt('your_test_data.txt') # load test dataset here



#    Now call the above defined functions to learn the SVM model using training 
#    data, use the learnt model to classify the test data and finally find the 
#    classification error of your learnt model. Store the error in a variable 
#    named ERROR. 

#    Write your code here to find ERROR





#==============================================================================


print ERROR
                   
                  








                      
