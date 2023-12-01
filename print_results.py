#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Mohamed Zayed Ahmed  
# DATE CREATED: 18th Nov. 2023    
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
import os
def print_results(results_dic, results_stats_dic, model,dir_path,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print(f"\n\n** Results Summary for {model.upper()} Model **")

    for key, value in results_stats_dic.items():
        print(f"{key}: {value}")

    if print_incorrect_dogs and (results_stats_dic['n_correct_dog_matches'] + results_stats_dic['n_correct_not_dog_matches'] != results_stats_dic['n_images']):
        print("\nIncorrect Dog/Not Dog Matches:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][0]}, Classified: {results_dic[key][1]}")

    if print_incorrect_breed and results_stats_dic['n_correct_dog_matches'] != results_stats_dic['n_correct_breed_matches']:
        print("\nIncorrect Breed Matches:")
        for key in results_dic:
            if results_dic[key][2] == 0 and results_dic[key][3] == 1:
                print(f"Real: {results_dic[key][0]}, Classified: {results_dic[key][1]}")
    # Define the data for the table
    data = [
       [model, results_stats_dic['pct_correct_notdogs'], results_stats_dic['pct_correct_dogs'], results_stats_dic['pct_correct_breed'], results_stats_dic['pct_label_matches']]]
    # Get the directory name
    dir_name = os.path.basename(dir_path.rstrip('/'))
     # Define the column titles
    column_titles = "{:<25} {:<25} {:<25} {:<25} {:<25}\n".format('Model', 'Pct Correct Not Dogs', 'Pct Correct Dogs', 'Pct Correct Breed', 'Pct Label Matches')
     # Open the file in append mode
    file_name = 'final_results_{}.txt'.format(dir_name)
    with open(file_name, 'a') as f:
         # Check if the file is empty
        if os.stat(file_name).st_size == 0:
             # Write the column titles
                f.write(column_titles)
         # Write the data
        for row in data:
            f.write("{:<25} {:<25} {:<25} {:<25} {:<25}\n".format(*row))
