%pip install tqdm
%pip install sympy
from sympy import *
import numpy as np
from tqdm import tqdm

# Define symbols
A, D, D11, D1m, D1n, D1p, D1q, D1r, D1v, D1w, D1y, D1z = symbols('A D D11 D1m D1n D1p D1q D1r D1v D1w D1y D1z')
D1g, D1h, D1i, D1j, D1k, D1l = symbols('D1g D1h D1i D1j D1k D1l')

D12, D22, D2m, D2n, D2p, D2q, D2r, D2v, D2w, D2y, D2z = symbols('D12 D22 D2m D2n D2p D2q D2r D2v D2w D2y D2z')
D2g, D2h, D2i, D2j, D2k, D2l = symbols('D2g D2h D2i D2j D2k D2l')

D13, D23, D33, D3m, D3n, D3p, D3q, D3r, D3v, D3w, D3y, D3z = symbols('D13 D23 D33 D3m D3n D3p D3q D3r D3v D3w D3y D3z')
D3g, D3h, D3i, D3j, D3k, D3l = symbols('D3g D3h D3i D3j D3k D3l')

D14, D24, D34, D4m, D4n, D4p, D4q, D4r, D4v, D4w, D4y, D4z = symbols('D14 D24 D34 D4m D4n D4p D4q D4r D4v D4w D4y D4z')
D44, D4g, D4h, D4i, D4j, D4k, D4l = symbols('D44 D4g D4h D4i D4j D4k D4l')

D15, D25, D35, D45, D5m, D5n, D5p, D5q, D5r, D5v, D5w, D5y, D5z = symbols('D15 D25 D35 D45 D5m D5n D5p D5q D5r D5v D5w D5y D5z')
D55, D5g, D5h, D5i, D5j, D5k, D5l = symbols('D55 D5g D5h D5i D5j D5k D5l')

J, Jg, Jh, Ji, Jj, Jk, Jl, Jm, Jn, Jp, Jq, Jr, Jv, Jw, Jy, Jz = symbols('J Jg Jh Ji Jj Jk Jl Jm Jn Jp Jq Jr Jv Jw Jy Jz')
Xi = Symbol('Xi')
Xi_func = exp(0.5 * J ** 2 * D)
expr = exp(0.5 * (J ** 2 * D))

new_expr = expr.subs({Xi_func: Xi})  # Doesn't replace with XI_function!!

# Function to 'differentiate' the Xi part of the expression
def differentiate_exponential(expression, vertex, intgrl_label):
    result = expression
    n = intgrl_label
    v = vertex

    # For 1st vertex, only maximum of 3 terms
    if (v == 1):
        if (n == 1):
            result = D1z * Jz * expression
        elif (n == 2):
            result = D1y * Jy * expression
        elif (n == 3):
            result = D1w * Jw * expression

    # For second vertex, maximum of 6 terms.
    elif (v == 2):
        if (n == 1):
            result = D2z * Jz * expression
        elif (n == 2):
            result = D2y * Jy * expression
        elif (n == 3):
            result = D2w * Jw * expression
        elif (n == 4):
            result = D2v * Jv * expression
        elif (n == 5):
            result = D2r * Jr * expression
        elif (n == 6):
            result = D2q * Jq * expression

    elif (v == 3):
        if (n == 1):
            result = D3z * Jz * expression
        elif (n == 2):
            result = D3y * Jy * expression
        elif (n == 3):
            result = D3w * Jw * expression
        elif (n == 4):
            result = D3v * Jv * expression
        elif (n == 5):
            result = D3r * Jr * expression
        elif (n == 6):
            result = D3q * Jq * expression
        elif (n == 7):
            result = D3p * Jp * expression
        elif (n == 8):
            result = D3n * Jn * expression
        elif (n == 9):
            result = D3m * Jm * expression

    elif (v == 4):
        if (n == 1):
            result = D4z * Jz * expression
        elif (n == 2):
            result = D4y * Jy * expression
        elif (n == 3):
            result = D4w * Jw * expression
        elif (n == 4):
            result = D4v * Jv * expression
        elif (n == 5):
            result = D4r * Jr * expression
        elif (n == 6):
            result = D4q * Jq * expression
        elif (n == 7):
            result = D4p * Jp * expression
        elif (n == 8):
            result = D4n * Jn * expression
        elif (n == 9):
            result = D4m * Jm * expression
        elif (n == 10):
            result = D4l * Jl * expression
        elif (n == 11):
            result = D4k * Jk * expression
        elif (n == 12):
            result = D4j * Jj * expression
            
    elif (v == 5):
        if (n == 1):
            result = D5z * Jz * expression
        elif (n == 2):
            result = D5y * Jy * expression
        elif (n == 3):
            result = D5w * Jw * expression
        elif (n == 4):
            result = D5v * Jv * expression
        elif (n == 5):
            result = D5r * Jr * expression
        elif (n == 6):
            result = D5q * Jq * expression
        elif (n == 7):
            result = D5p * Jp * expression
        elif (n == 8):
            result = D5n * Jn * expression
        elif (n == 9):
            result = D5m * Jm * expression
        elif (n == 10):
            result = D5l * Jl * expression
        elif (n == 11):
            result = D5k * Jk * expression
        elif (n == 12):
            result = D5j * Jj * expression
        elif (n == 13):
            result = D5i * Ji * expression
        elif (n == 14):
            result = D5h * Jh * expression
        elif (n == 15):
            result = D5g * Jg * expression

    return result
    
    # Function to 'differentiate' the J term
def differentiate_J(expression, vertex_to_be_paired, whichJ):
    result = expression
    vertex = vertex_to_be_paired
    n = whichJ
    if vertex == 1:
        if (n == 1):
            result = D11 * expression.diff(Jz) / D1z
        elif (n == 2):
            result = D11 * expression.diff(Jy) / D1y
        elif (n == 3):
            result = D11 * expression.diff(Jw) / D1w

    elif vertex == 2:
        if (n == 1):
            result = D12 * expression.diff(Jz).diff(D1z) + D22 * expression.diff(Jz).diff(D2z)
        elif (n == 2):
            result = D12 * expression.diff(Jy).diff(D1y) + D22 * expression.diff(Jy).diff(D2y)
        elif (n == 3):
            result = D12 * expression.diff(Jw).diff(D1w) + D22 * expression.diff(Jw).diff(D2w)
        elif (n == 4):
            result = D12 * expression.diff(Jv).diff(D1v) + D22 * expression.diff(Jv).diff(D2v)
        elif (n == 5):
            result = D12 * expression.diff(Jr).diff(D1r) + D22 * expression.diff(Jr).diff(D2r)
        elif (n == 6):
            result = D12 * expression.diff(Jq).diff(D1q) + D22 * expression.diff(Jq).diff(D2q)

    elif vertex == 3:
        if (n == 1):
            result = D13 * expression.diff(Jz).diff(D1z) \
                     + D23 * expression.diff(Jz).diff(D2z) + D33 * expression.diff(Jz).diff(D3z)
        elif (n == 2):
            result = D13 * expression.diff(Jy).diff(D1y) \
                     + D23 * expression.diff(Jy).diff(D2y) + D33 * expression.diff(Jy).diff(D3y)
        elif (n == 3):
            result = D13 * expression.diff(Jw).diff(D1w) \
                     + D23 * expression.diff(Jw).diff(D2w) + D33 * expression.diff(Jw).diff(D3w)
        elif (n == 4):
            result = D13 * expression.diff(Jv).diff(D1v) \
                     + D23 * expression.diff(Jv).diff(D2v) + D33 * expression.diff(Jv).diff(D3v)
        elif (n == 5):
            result = D13 * expression.diff(Jr).diff(D1r) \
                     + D23 * expression.diff(Jr).diff(D2r) + D33 * expression.diff(Jr).diff(D3r)
        elif (n == 6):
            result = D13 * expression.diff(Jq).diff(D1q) \
                     + D23 * expression.diff(Jq).diff(D2q) + D33 * expression.diff(Jq).diff(D3q)
        elif (n == 7):
            result = D13 * expression.diff(Jp).diff(D1p) \
                     + D23 * expression.diff(Jp).diff(D2p) + D33 * expression.diff(Jz).diff(D3p)
        elif (n == 8):
            result = D13 * expression.diff(Jn).diff(D1n) \
                     + D23 * expression.diff(Jn).diff(D2n) + D33 * expression.diff(Jn).diff(D3n)
        elif (n == 9):
            result = D13 * expression.diff(Jm).diff(D1m) \
                     + D23 * expression.diff(Jm).diff(D2m) + D33 * expression.diff(Jm).diff(D3m)

    elif vertex == 4:
        if (n == 1):
            result = D14 * expression.diff(Jz).diff(D1z) \
                     + D24 * expression.diff(Jz).diff(D2z) + D34 * expression.diff(Jz).diff(D3z) \
                     + D44 * expression.diff(Jz).diff(D4z)
        elif (n == 2):
            result = D14 * expression.diff(Jy).diff(D1y) \
                     + D24 * expression.diff(Jy).diff(D2y) + D34 * expression.diff(Jy).diff(D3y) \
                     + D44 * expression.diff(Jy).diff(D4y)
        elif (n == 3):
            result = D14 * expression.diff(Jw).diff(D1w) \
                     + D24 * expression.diff(Jw).diff(D2w) + D34 * expression.diff(Jw).diff(D3w) \
                     + D44 * expression.diff(Jw).diff(D4w)
        elif (n == 4):
            result = D14 * expression.diff(Jv).diff(D1v) \
                     + D24 * expression.diff(Jv).diff(D2v) + D34 * expression.diff(Jv).diff(D3v) \
                     + D44 * expression.diff(Jv).diff(D4v)
        elif (n == 5):
            result = D14 * expression.diff(Jr).diff(D1r) \
                     + D24 * expression.diff(Jr).diff(D2r) + D34 * expression.diff(Jr).diff(D3r) \
                     + D44 * expression.diff(Jr).diff(D4r)
        elif (n == 6):
            result = D14 * expression.diff(Jq).diff(D1q) \
                     + D24 * expression.diff(Jq).diff(D2q) + D34 * expression.diff(Jq).diff(D3q) \
                     + D44 * expression.diff(Jq).diff(D4q)
        elif (n == 7):
            result = D14 * expression.diff(Jp).diff(D1p) \
                     + D24 * expression.diff(Jp).diff(D2p) + D34 * expression.diff(Jp).diff(D3p) \
                     + D44 * expression.diff(Jp).diff(D4p)
        elif (n == 8):
            result = D14 * expression.diff(Jn).diff(D1n) \
                     + D24 * expression.diff(Jn).diff(D2n) + D34 * expression.diff(Jn).diff(D3n) \
                     + D44 * expression.diff(Jn).diff(D4n)
        elif (n == 9):
            result = D14 * expression.diff(Jm).diff(D1m) \
                     + D24 * expression.diff(Jm).diff(D2m) + D34 * expression.diff(Jm).diff(D3m) \
                     + D44 * expression.diff(Jm).diff(D4m)
        elif (n == 10):
            result = D14 * expression.diff(Jl).diff(D1l) \
                     + D24 * expression.diff(Jl).diff(D2l) + D34 * expression.diff(Jl).diff(D3l) \
                     + D44 * expression.diff(Jl).diff(D4l)
        elif (n == 11):
            result = D14 * expression.diff(Jk).diff(D1k) \
                     + D24 * expression.diff(Jk).diff(D2k) + D34 * expression.diff(Jk).diff(D3k) \
                     + D44 * expression.diff(Jk).diff(D4k)
        elif (n == 12):
            result = D14 * expression.diff(Jj).diff(D1j) \
                     + D24 * expression.diff(Jj).diff(D2j) + D34 * expression.diff(Jj).diff(D3j) \
                     + D44 * expression.diff(Jj).diff(D4j)
            
        
    elif vertex == 5:
        if (n == 1):
            result = D15 * expression.diff(Jz).diff(D1z) \
                     + D25 * expression.diff(Jz).diff(D2z) + D35 * expression.diff(Jz).diff(D3z) \
                     + D45 * expression.diff(Jz).diff(D4z) + D55 * expression.diff(Jz).diff(D5z)
        elif (n == 2):
            result = D15 * expression.diff(Jy).diff(D1y) \
                     + D25 * expression.diff(Jy).diff(D2y) + D35 * expression.diff(Jy).diff(D3y) \
                     + D45 * expression.diff(Jy).diff(D4y) + D55 * expression.diff(Jy).diff(D5y)
        elif (n == 3):
            result = D15 * expression.diff(Jw).diff(D1w) \
                     + D25 * expression.diff(Jw).diff(D2w) + D35 * expression.diff(Jw).diff(D3w) \
                     + D45 * expression.diff(Jw).diff(D4w) + D55 * expression.diff(Jw).diff(D5w)
        elif (n == 4):
            result = D15 * expression.diff(Jv).diff(D1v) \
                     + D25 * expression.diff(Jv).diff(D2v) + D35 * expression.diff(Jv).diff(D3v) \
                     + D45 * expression.diff(Jv).diff(D4v) + D55 * expression.diff(Jv).diff(D5v)
        elif (n == 5):
            result = D15 * expression.diff(Jr).diff(D1r) \
                     + D25 * expression.diff(Jr).diff(D2r) + D35 * expression.diff(Jr).diff(D3r) \
                     + D45 * expression.diff(Jr).diff(D4r) + D55 * expression.diff(Jr).diff(D5r)
        elif (n == 6):
            result = D15 * expression.diff(Jq).diff(D1q) \
                     + D25 * expression.diff(Jq).diff(D2q) + D35 * expression.diff(Jq).diff(D3q) \
                     + D45 * expression.diff(Jq).diff(D4q) + D55 * expression.diff(Jq).diff(D5q)
        elif (n == 7):
            result = D15 * expression.diff(Jp).diff(D1p) \
                     + D25 * expression.diff(Jp).diff(D2p) + D35 * expression.diff(Jp).diff(D3p) \
                     + D45 * expression.diff(Jp).diff(D4p) + D55 * expression.diff(Jp).diff(D5p)
        elif (n == 8):
            result = D15 * expression.diff(Jn).diff(D1n) \
                     + D25 * expression.diff(Jn).diff(D2n) + D35 * expression.diff(Jn).diff(D3n) \
                     + D45 * expression.diff(Jn).diff(D4n) + D55 * expression.diff(Jn).diff(D5n)
        elif (n == 9):
            result = D15 * expression.diff(Jm).diff(D1m) \
                     + D25 * expression.diff(Jm).diff(D2m) + D35 * expression.diff(Jm).diff(D3m) \
                     + D45 * expression.diff(Jm).diff(D4m) + D55 * expression.diff(Jm).diff(D5m)
        elif (n == 10):
            result = D15 * expression.diff(Jl).diff(D1l) \
                     + D25 * expression.diff(Jl).diff(D2l) + D35 * expression.diff(Jl).diff(D3l) \
                     + D45 * expression.diff(Jl).diff(D4l) + D55 * expression.diff(Jl).diff(D5l)
        elif (n == 11):
            result = D15 * expression.diff(Jk).diff(D1k) \
                     + D25 * expression.diff(Jk).diff(D2k) + D35 * expression.diff(Jk).diff(D3k) \
                     + D45 * expression.diff(Jk).diff(D4k) + D55 * expression.diff(Jk).diff(D5k)
        elif (n == 12):
            result = D15 * expression.diff(Jj).diff(D1j) \
                     + D25 * expression.diff(Jj).diff(D2j) + D35 * expression.diff(Jj).diff(D3j) \
                     + D45 * expression.diff(Jj).diff(D4j) + D55 * expression.diff(Jj).diff(D5j)
        elif (n == 13):
            result = D15 * expression.diff(Ji).diff(D1i) \
                     + D25 * expression.diff(Ji).diff(D2i) + D35 * expression.diff(Ji).diff(D3i) \
                     + D45 * expression.diff(Ji).diff(D4i) + D55 * expression.diff(Ji).diff(D5i)
        elif (n == 14):
            result = D15 * expression.diff(Jh).diff(D1h) \
                     + D25 * expression.diff(Jh).diff(D2h) + D35 * expression.diff(Jh).diff(D3h) \
                     + D45 * expression.diff(Jh).diff(D4h) + D55 * expression.diff(Jh).diff(D5h)
        elif (n == 15):
            result = D15 * expression.diff(Jg).diff(D1g) \
                     + D25 * expression.diff(Jg).diff(D2g) + D35 * expression.diff(Jg).diff(D3g) \
                     + D45 * expression.diff(Jg).diff(D4g) + D55 * expression.diff(Jg).diff(D5g)
    return result
    
# Function to group equivalent terms
def group_equal_graphs(expression, vertex_number, bool_search_specific_graph, number_source_terms_desired, discard_bubble_terms):
    """
    
    vertex_number is how many edges connect two vertices, minus one, in desired graph. Use number of edges of the vertex order to remove disconnected graphs.
    Bool_search_graph is true if wanting to search for a specific graph.
    number_source_terms_desired is the number of source terms in the desired graph. (all terms without this exact number
    of sources will be discarded).
    """
    vertex = vertex_number
    #print("\nInput expression is : ", expression)
    str_expr = expression.replace(" ", "").split("+")  #str(expression.expand())  # Use this if input expression is a SymPy object instead of string.
    # print(str_expr)
    # print("\nString is: ", str_expr, "\n")
    master_arr = np.ones(len(str_expr))
    # print(master_arr)
    master_list = []

    # Create Master list
    for i in range(len(str_expr)):
        list_term = str_expr[i].split("*")
        # print(type(list_term[i]))
        master_list.append(list_term)

    #print(type(master_list[0][1]))
    #print("\nMASTER LIST : \n", master_list)

    #Index to delete terms that are not from desired graph

    #print("MASTER ARRAY : \n", master_array)
    #print(master_keep_term)
    #print(len(master_list))
    master_keep_term = np.full(len(master_list), True)#np.full(len(master_list), True)  # True to keep, false to delete
    #print(master_keep_term)
    #print("HERE : \n", master_keep_term.size)


    # Work through each item in list
    for i in tqdm(range(len(master_list))):
        #print("\nWAS :", master_list[i])
        J_count = 0
        sub_count = 0
        source_to_vertex_count = 0
        # print("\n\n", master_list[i])

        # Booleans to see which source terms are already present
        z_bool, y_bool, w_bool, v_bool, r_bool, q_bool, p_bool, n_bool, m_bool, l_bool, k_bool, j_bool, i_bool, h_bool, g_bool \
            = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
        bool_array = \
            np.array([z_bool, y_bool, w_bool, v_bool, r_bool, q_bool, p_bool, n_bool, m_bool, l_bool, k_bool, j_bool, i_bool, h_bool, g_bool])

        source_term_arr = np.array(['Jz', 'Jy', 'Jw', 'Jv', 'Jr', 'Jq', 'Jp', 'Jn', 'Jm', 'Jl', 'Jk', 'Jj', 'Ji', 'Jh', 'Jg'])


        delta1_array = np.array(['D1z', 'D1y', 'D1w', 'D1v', 'D1r', 'D1q', 'D1p', 'D1n', 'D1m', 'D1l', 'D1k', 'D1j', 'D1i', 'D1h', 'D1g'])
        delta2_array = np.array(['D2z', 'D2y', 'D2w', 'D2v', 'D2r', 'D2q', 'D2p', 'D2n', 'D2m', 'D2l', 'D2k', 'D2j', 'D2i', 'D2h', 'D2g'])
        delta3_array = np.array(['D3z', 'D3y', 'D3w', 'D3v', 'D3r', 'D3q', 'D3p', 'D3n', 'D3m', 'D3l', 'D3k', 'D3j', 'D3i', 'D3h', 'D3g'])
        delta4_array = np.array(['D4z', 'D4y', 'D4w', 'D4v', 'D4r', 'D4q', 'D4p', 'D4n', 'D4m', 'D4l', 'D4k', 'D4j', 'D4i', 'D4h', 'D4g'])
        delta5_array = np.array(['D5z', 'D5y', 'D5w', 'D5v', 'D5r', 'D5q', 'D5p', 'D5n', 'D5m', 'D5l', 'D5k', 'D5j', 'D5i', 'D5h', 'D5g'])

        # Get correct J_count (number of sources
        for j in range(len(master_list[i])):
            el = master_list[i][j]

            # print(el)
            if (el == 'Jg') or (el == 'Jh') or (el == 'Ji') or (el == 'Jj') or \
                    (el == 'Jk') or (el == 'Jl') or (el == 'Jm') or (el == 'Jn') or (el == 'Jp') or \
                    (el == 'Jv') or (el == 'Jw') or (el == 'Jr') or (el == 'Jq') or (el == 'Jy') or (el == 'Jz'):
                J_count += 1

        #print(J_count)
        # Don't run remaining code if current graph doesn't contain specific number of sources
        if bool_search_specific_graph and (J_count != number_source_terms_desired):
            master_keep_term[i] = False
            continue
        #print("J count is : ", J_count)

        new_source_arr = source_term_arr[0:J_count]

        #  The sub count is how many of the J terms do not need to be changed as they are in the correct order (Jz, Jy, Jw, ... )
        for n in range(len(master_list[i])):
            el = master_list[i][n]
            #X_ARRAY = bool_array

            #Gives index of which source term has been matched
            sub_count += np.where(new_source_arr == el)[0].size

        # Correct the J terms to be in the correct order.
        for j in range(J_count):
            master_list[i][-2 - j] = new_source_arr[j]

        #print(source_term_arr)
        #print("BOOL ARRAY : ", bool_array)
        #print(type(source_term_arr[bool_array][0]))
        #print("SubCount is : ", sub_count)
        #print("Delta array", delta2_array[np.logical_not(bool_array)])

        super_delta_array = np.array([delta1_array, delta2_array, delta3_array, delta4_array, delta5_array])

        # Replace terms and place each term in standard order
        for j in range(len(master_list[i])):
            el = master_list[i][j]
            #print(el)
            # Create super delta array of all terms that are to be replaced
            # super_delta_array_cut = np.array([delta1_array[sub_count:], delta2_array[sub_count:], delta3_array[sub_count:], delta4_array[sub_count:]])

            #Find what symbol the current element is
            indices_asdf = np.where(super_delta_array == el)
            indices_source = np.where(source_term_arr == el)

            #print(indices_asdf, indices_source)

            # Skip to next item in loop if hit a source term, or constant.
            if (not indices_asdf[0].size > 0) or (indices_source[0].size > 0):
                continue

            # Find the indices of the current element in the super delta array
            indices_replace = np.array([indices_asdf[0][0], indices_asdf[1][0]])  # First term is D1, D2, D3, D4 etc, second term is which source z,y,w,v etc

            # Check if master_list item should be replaced with another item that is the correct order (Dz, Dy, Dw etc.)
            #print(indices_replace[1], sub_count)
            if (indices_source[0].size == 0):
                #print("STVC count", source_to_vertex_count)
                #print("here")
                master_list[i][j] = super_delta_array[indices_replace[0]][source_to_vertex_count]
                sub_count += 1
            #should only reach here if source-vertex term
            source_to_vertex_count += 1

        #print("NOW :", master_list[i], "\n")

    # print("\n\nMaster List: \n", master_list)
    #Produce output
    output = ""
    #print("MASTER LIST: ", master_list)
    #Find disconnected terms
    for i in range(len(master_list)):
        if not master_keep_term[i]:
            continue
        """
        For a connected diagram it must be possible to reach every vertex from any other one. This means that there must be
        at least (N-1) propagators joining vertices.
        """
        #For N vertices, need to have (N-1) cross terms. Discard disconnected pieces.
        x12_bool, x_13, x_14, x_15, x_23, x_24, x_25, x_34, x_35, x_45 = False, False, False, False, False, False, False, False, False, False,
        #vertex_connected_bool_array
        vcba = np.array([x12_bool, x_13, x_14, x_15, x_23, x_24, x_25, x_34, x_35, x_45])
        contain_bubble = False
        #Count propagators between vertices and find in term contains bubbles.
        for k in range(len(master_list[i])):
            if master_list[i][k] == 'D12':
                vcba[0] = True
            elif master_list[i][k] == 'D13':
                vcba[1] = True
            elif master_list[i][k] == 'D14':
                vcba[2] = True
            elif master_list[i][k] == 'D15':
                vcba[2] = True
            elif master_list[i][k] == 'D23':
                vcba[3] = True
            elif master_list[i][k] == 'D24':
                vcba[4] = True
            elif master_list[i][k] == 'D25':
                vcba[4] = True
            elif master_list[i][k] == 'D34':
                vcba[5] = True
            elif master_list[i][k] == 'D35':
                vcba[5] = True
            elif master_list[i][k] == 'D45':
                vcba[5] = True
            elif master_list[i][k] == 'D11':
                contain_bubble = True
            elif master_list[i][k] == 'D22':
                contain_bubble = True
            elif master_list[i][k] == 'D33':
                contain_bubble = True
            elif master_list[i][k] == 'D44':
                contain_bubble = True
            elif master_list[i][k] == 'D55':
                contain_bubble = True

        # If term is disconnected, element in master_keep_term array is False
        if discard_bubble_terms and ((np.count_nonzero(vcba) < (vertex-1)) or contain_bubble):
            master_keep_term[i] = False

    # # delete terms that are disconnected/ don't fit desired graph:
    # print("\n\n", master_keep_term, "\n\n")
    # print("Sizes : \n ", master_keep_term.size)
    # print("Size : \n", master_array.size)
    # print("Type: ", master_keep_term.dtype)
    master_array = np.array([np.array(i) for i in master_list]) # RIght now this is an array of arrays

    master_array = master_array[master_keep_term]
    #print(master_array)

    #Create output
    for i in range(len(master_array)):
        for j in range(len(master_array[i]) - 1):
            output += str(master_array[i][j]) + "*"
        if i < (len(master_array) - 1):
            output += str(master_array[i][-1]) + " + "
        else:
            output += str(master_array[i][-1])

    #print("Output : ", output)
    return sympify(output)
    
# Solve for V=1
def differentiate_one_vertex():

    Diff1 = differentiate_exponential(Xi_func, 1, 1)
        
    Diff2 = differentiate_J(Diff1, 1, 1) + differentiate_exponential(Diff1, 1, 2)
        
    Diff3 = differentiate_J(Diff2, 1, 1) + differentiate_J(Diff2, 1, 2) + differentiate_exponential(Diff2, 1, 3)
    
    Diff3_with_Xi = Diff3.subs({Xi_func: Xi}).expand()

    return Diff3_with_Xi.expand()

# Solve for V=2
def differentiate_two_vertices(resultFromV1):
    V1 = resultFromV1

    Diff1 = differentiate_J(V1, 2, 1) + differentiate_J(V1, 2, 2) + differentiate_J(V1, 2, 3) + differentiate_exponential(V1, 2, 4)
    
    Diff2 = differentiate_J(Diff1, 2, 1) + differentiate_J(Diff1, 2, 2) + differentiate_J(Diff1, 2, 3) \
            + differentiate_J(Diff1, 2, 4) + differentiate_exponential(Diff1, 2, 5)
    
    Diff3 = differentiate_J(Diff2, 2, 1) + differentiate_J(Diff2, 2, 2) + differentiate_J(Diff2, 2, 3) \
            + differentiate_J(Diff2, 2, 4) + differentiate_J(Diff2, 2, 5) + differentiate_exponential(Diff2, 2, 6)

    Diff3_with_Xi = Diff3.subs({Xi_func: Xi}).expand()
    
    return Diff3_with_Xi.expand()
    
# Solve for V=3
def differentiate_three_vertices(resultFromV2):
    V2 = resultFromV2
    
    Diff1 = differentiate_J(V2, 3, 1) + differentiate_J(V2, 3, 2) + differentiate_J(V2, 3, 3) + differentiate_J(V2, 3, 4) + differentiate_J(V2, 3, 5) + differentiate_J(V2, 3, 6) + differentiate_exponential(V2, 3, 7)

    Diff2 = differentiate_J(Diff1, 3, 1) + differentiate_J(Diff1, 3, 2) + differentiate_J(Diff1, 3, 3) + differentiate_J(Diff1, 3, 4) + differentiate_J(Diff1, 3, 5) + differentiate_J(Diff1, 3, 6) + differentiate_J(Diff1, 3, 7) + differentiate_exponential(Diff1, 3, 8)

    Diff3 = differentiate_J(Diff2, 3, 1) + differentiate_J(Diff2, 3, 2) + differentiate_J(Diff2, 3, 3) + differentiate_J(Diff2, 3, 4) + differentiate_J(Diff2, 3, 5) + differentiate_J(Diff2, 3, 6) + differentiate_J(Diff2, 3, 7) + differentiate_J(Diff2, 3, 8) + differentiate_exponential(Diff2, 3, 9)

    Diff3_with_Xi = Diff3.subs({Xi_func: Xi}).expand()
    
    return Diff3_with_Xi.expand()

# Solve for V=4. 
def differentiate_four_vertices(resultFromV3):
    V3 = resultFromV3

    Diff1 = differentiate_J(V3, 4, 1) + differentiate_J(V3, 4, 2) + differentiate_J(V3, 4, 3) + \
            differentiate_J(V3, 4, 4) + differentiate_J(V3, 4, 5) + differentiate_J(V3, 4, 6) + \
            differentiate_J(V3, 4, 7) + differentiate_J(V3, 4, 8) + differentiate_J(V3, 4, 9) + \
            differentiate_exponential(V3, 4, 10)

    print("First derivative DONE \n")
    
    Diff2 = differentiate_J(Diff1, 4, 1) + differentiate_J(Diff1, 4, 2) + differentiate_J(Diff1, 4, 3) + \
            differentiate_J(Diff1, 4, 4) + differentiate_J(Diff1, 4, 5) + differentiate_J(Diff1, 4, 6) + \
            differentiate_J(Diff1, 4, 7) + differentiate_J(Diff1, 4, 8) + differentiate_J(Diff1, 4, 9) + \
            differentiate_J(Diff1, 4, 10) + differentiate_exponential(Diff1, 4, 11)

    print("Second derivative DONE \n")
    
    Diff3 = differentiate_J(Diff2, 4, 1) + differentiate_J(Diff2, 4, 2) + differentiate_J(Diff2, 4, 3) + \
            differentiate_J(Diff2, 4, 4) + differentiate_J(Diff2, 4, 5) + differentiate_J(Diff2, 4, 6) + \
            differentiate_J(Diff2, 4, 7) + differentiate_J(Diff2, 4, 8) + differentiate_J(Diff2, 4, 9) + \
            differentiate_J(Diff2, 4, 10) + differentiate_J(Diff2, 4, 11) + differentiate_exponential(Diff2, 4, 12)
    Diff3_with_Xi = Diff3.subs({Xi_func: Xi}).expand()
    
    print("Third derivative DONE \n")

    return Diff3_with_Xi.expand()
# Solve for V=5. 
def differentiate_five_vertices(resultFromV4):
    V4 = resultFromV4

    Diff1 = differentiate_J(V4, 5, 1) + differentiate_J(V4, 5, 2) + differentiate_J(V4, 5, 3) + \
            differentiate_J(V4, 5, 4) + differentiate_J(V4, 5, 5) + differentiate_J(V4, 5, 6) + \
            differentiate_J(V4, 5, 7) + differentiate_J(V4, 5, 8) + differentiate_J(V4, 5, 9) + \
            differentiate_J(V4, 5, 10) + differentiate_J(V4, 5, 11) + differentiate_J(V4, 5, 12) + \
            differentiate_exponential(V4, 5, 13)

    print("First derivative DONE \n")
    
    Diff2 = differentiate_J(Diff1, 5, 1) + differentiate_J(Diff1, 5, 2) + differentiate_J(Diff1, 5, 3) + \
            differentiate_J(Diff1, 5, 4) + differentiate_J(Diff1, 5, 5) + differentiate_J(Diff1, 5, 6) + \
            differentiate_J(Diff1, 5, 7) + differentiate_J(Diff1, 5, 8) + differentiate_J(Diff1, 5, 9) + \
            differentiate_J(Diff1, 5, 10) + differentiate_J(Diff1, 5, 11) + differentiate_J(Diff1, 5, 12) + \
            differentiate_J(Diff1, 5, 13) + differentiate_exponential(Diff1, 5, 14)

    print("Second derivative DONE \n")
    
    Diff3 = differentiate_J(Diff2, 5, 1) + differentiate_J(Diff2, 5, 2) + differentiate_J(Diff2, 5, 3) + \
            differentiate_J(Diff2, 5, 4) + differentiate_J(Diff2, 5, 5) + differentiate_J(Diff2, 5, 6) + \
            differentiate_J(Diff2, 5, 7) + differentiate_J(Diff2, 5, 8) + differentiate_J(Diff2, 5, 9) + \
            differentiate_J(Diff2, 5, 10) + differentiate_J(Diff2, 5, 11) + differentiate_J(Diff2, 5, 12) + \
            differentiate_J(Diff2, 5, 13) + differentiate_J(Diff2, 5, 14) +  differentiate_exponential(Diff2, 5, 15)
    Diff3_with_Xi = Diff3.subs({Xi_func: Xi}).expand()
    
    print("Third derivative DONE \n")

    return Diff3_with_Xi.expand()

