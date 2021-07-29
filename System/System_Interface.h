#ifndef _SYSTEM_INTERFACE_H_
#define _SYSTEM_INTERFACE_H_	
	/*****************************************************************************
	* Function Name :             Edit_patient
	* Function Description :      Function to Edit patient data by using ID, 
	* [args] :                    void
	* [in] :                      Address of first Node in Linked List
	*	  
	* [out] :                     updated patient's data 				
	*							  
	* [in/out] :				  None
	* [Returns] :			      void
	*******************************************************************************/
	void Edit_patient(void);
	/*******************************************************************************
	* Function Name :             Cancel_resrve
	* Function Description :      Function to Cancel The resrvation of patiant
	* [args] :                    void
					  
	* [Returns] :			      void
	********************************************************************************/
	void Cancel_resrve(void);	
	/*******************************************************
	* Function Name :             Print_patient_list
	* Function Description :      Function to print patients data
	* [args] :                    void
	* [in] :                      Address of first Node in Linked List
	*							  
	* [out] :                     patients data 				
	*							  
	* [in/out] :				  None
	* [Returns] :			      void
	*******************************************************/
	void Print_patient_list(void);
	/***************************
	* Function Name :             Patient_record
	* Function Description :      Function to search for patient data by using ID, 
	* [args] :                    void
	*	  
	* [out] :                      print patient's data 				
	*							  
	* [in/out] :				  None
	* [Returns] :			      void
	***************************/
	void Patient_record(void);
	/***************************
	* Function Name :             Add_patient
	* Function Description :      Function to add patient data by using ID, 
	* [args] :                    void
	*	  
	* [out] :                     add patient's data 				
	*							  
	* [in/out] :				  None
	* [Returns] :			      void
	***************************/
	void Add_patient(void);	
	
	
	/********************not commented yet*****************/
	// view all reserved slots
	void View_reserve(void);
	// reserve slot for specefic patient
	void Reserve_slot(void);    // Number of avialable slots  > 0
#endif

