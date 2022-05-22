**JFinder - Similar JIRA Finder**

**Abstract:** 
Resolution time of a bug/enhancement is a key factor when it comes to fixing an issue which directly affect the customer satisfaction and resource usage within the organization. It is common to see that similar JIRAs are filed each day by different customers/AEs/PVs. Current process for filing a JIRA involves PV/AE searching for similar issues existing in the JIRA system using JQL and his/her prior knowledge/heuristic. This mechanism is not a well-suited approach as JQL is a difficult art to master and not a common knowledge among PVs/AEs. JIRA similarity is mostly tracked based on the component owner’s and AE’s/PV’s prior experience. Hence there is a strong possibility that PV/AE is missing to find the similar JIRA and filing the same JIRA again. Current high number of JIRAs in the system (more than 22,000) also contributed to this. When this happens both PV/AE and RnD have to spend additional time to reproduce, fix and validate the issues. Additional time might have been already utilized when they get to know the issue is a duplicate which was already fixed in some other JIRA. 
Our approach is to build a tool which can be used by both PV/AE and RnD to identify the similar JIRAs in the initial phase of the JIRA tracking to reduce the overall development and validation time.



**Solution:** 
Propose a ML based utility which can search existing JIRAs which fits best for the interest of search based on Summary and Description. The utility is capable to predict the similar issues based on given Summary/Description or JIRA id.


**Productivity improvement:** 

- Speedup the development/validation time 
    If there are similar root cause RnD can refer it.
    PV/AE could leverage existing similar test plans and test cases.

- Save the turnaround time.
- Customer issues could be analyzed whether it is known or a real issue. If a known issue, solution/work around could be provided by looking at the similar JIRAs.



**Existing Solution:**

There is an existing extension for the similar task provided by Atlassian. Synopsys has not incorporated it into the current JIRA infrastructure. 
Extension is expensive.
https://marketplace.atlassian.com/apps/1212538/similar-issues-finder?tab=overview&hosting=datacenter

There was a similar utility on Synopsys for CRM :
https://sp-vg/sites/PV-Verdi/_layouts/15/WopiFrame.aspx?sourcedoc=/sites/PV-Verdi/Shared%20Documents/Innovation/ML_STAR_PV_RCA_Phase_I_YunxXiang_0821.pptx&action=default

**Team Members:**
- Charitha Senarathne (Mentor)
- Asitha Sandakalum
- Gayan VGT  
- Nalaka Jayanath
- Rehani Rodrigo


