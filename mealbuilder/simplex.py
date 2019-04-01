
import math
import numpy as np
from numpy import linalg as la
from .models import Food, Meal, MealItem

def vertcat(arr1,arr2):
    return np.concatenate((arr1,arr2),axis=0)
def horzcat(arr1,arr2):
    return np.concatenate((arr1,arr2),axis=1)

def findPivotRow(T,pivotColumn,lastColumn,m):
    min = float('inf')
    for i in range(m):
        if T[i,pivotColumn] > 0:
            quotient = T[i,lastColumn]/T[i,pivotColumn]
            if quotient<min:
                min = quotient
                pivotRow = i
    return pivotRow

def gaussianElimination(T,pRow,pCol,m):
    T[pRow] = T[pRow]/T[pRow,pCol]
    for i in range(m):
        if i!=pRow:
            T[i] = T[i] - T[pRow]*T[i,pCol]
    return T

def findPivotColumn(T,m,n):
    pivotColumn = -1
    min = -1e-5
    for i in range(m):
        for j in range(n):
            if T[i,j] < min:
                min = T[i,j]
                pivotColumn = j
    return pivotColumn

def simplexSolution(T,mC,nC,mT,nT):
    x = np.zeros((nC,1),dtype=float)
    for j in range(nC):
        cont = True
        found = -1
        for i in range(mT):
            if T[i,j]==1.0 and found==-1:
                found = i
            elif T[i,j]==0.0:
                cont = True
            else:
                cont = False
                break
        if cont and found!=-1 and i==mT-1:
            x[j,0] = T[found,nT-1]
    print(x)
    return x

def simplexMacro(Foods,Constraints,upperBounds):
    goalMacros = upperBounds[0:3]
    (mF,nF) = np.shape(Foods)
    (mC,nC) = np.shape(Constraints)

    tableau = horzcat(horzcat(vertcat(Constraints, -Foods),np.eye(mF+mC)),vertcat(upperBounds,np.zeros((mF,1),dtype=float)))
    (mT,nT) = np.shape(tableau)

    pivotColumn = findPivotColumn(tableau[mC:mT,0:nT-1],mF,nT-1)
    pivotCount = 1
    while pivotColumn!=-1 and pivotCount<=nC:
        pivotRow = findPivotRow(tableau,pivotColumn,nT-1,mC)
        tableau = gaussianElimination(tableau,pivotRow,pivotColumn,mT)
        pivotCount = pivotCount+1
        pivotColumn = findPivotColumn(tableau[mC:mT,0:nT-1],mF,nT-1)

    servingSizes = simplexSolution(tableau,mC,nC,mT,nT)
    mealMacros = tableau[mT-mF:mT-1,nT-1]
    carryOver = goalMacros - mealMacros
    #if goalMacros != np.array([[0],[0],[0]]):
        #mealQuality = la.norm(mealMacros - goalMacros)/la.norm(goalMacros)
    #else:
        #mealQuality = 0

    return servingSizes

#gets context from the meal builder form?
def OptimizeMeal(meal):

    #import ipdb; ipdb.set_trace()

    #how to access just the mealitems with the foreign key to this meal?


    goalMacros = np.zeros((3,1),dtype=float)
    goalMacros[0,0] = meal.protein_goal
    goalMacros[1,0] = meal.carb_goal
    goalMacros[2,0] = meal.fat_goal

    mealItems = meal.mealitem_set.all()
    numberOfFoods = mealItems.count()
    foodComposition = np.zeros((3,numberOfFoods),dtype=float)
    upperBounds = np.zeros((numberOfFoods,1),dtype=float)

    for i in range(numberOfFoods):
        protein = mealItems[i].food.protein
        carbs = mealItems[i].food.carbs
        fat = mealItems[i].food.fat
        foodComposition[:,i] = np.array([[protein,carbs,fat]])

        foodLimit = mealItems[i].limit
        if foodLimit is None:
            upperBounds[i,0] = float('inf')
        else:
            upperBounds[i,0] = foodLimit

    lConstraints = vertcat(foodComposition,np.eye(numberOfFoods)*100)
    rConstraints = vertcat(goalMacros,upperBounds)
    servingSizes=simplexMacro(foodComposition,lConstraints,rConstraints)

    for i in range(numberOfFoods):
        item = mealItems[i]
        item.quantity = servingSizes[i,0]
        item.updateNutrients()

    meal.updateNutrients()
    meal.save()
    return meal
