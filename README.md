# BCA Public Criminal Conviction Data

## About Hearth Connection

Hearth Connection is an innovative, data-driven nonprofit located in Saint Paul dedicated to ending long-term homelessness in Minnesota. Offering services and affordable housing, our collaborative projects serve over 1,300 children, adults, and youth each year to break the cycle of homelessness and achieve housing stability and health recovery. Driven by data, we focus on solutions that improve outcomes for participants and communities. We are a small, fast-moving organization that values creative thinking and is very committed to its mission.

## Project context

Hearth Connection needs to prove the impact our program has on improving outcomes for our participants and their communities. Evidence shows (http://www.hearthconnection.org/research/) we do this by shifting "bad" costs (hospitalization, incaceration, crime) to "good" costs (housing, case worker support) and ultimately reduce overall cost. To measure our participants' involvement in the criminal justice system pre- and post-enrollment, we have obtained a large data source of public criminal conviction data from the Minnesota Bureau of Criminal Apprehension (BCA).

The data source obtained is a single XML file. To make this usable, we aim to write a reusable script (these data are available as monthly releases with minimal or no schema changes) that converts the data into a more efficiently accessible format, preferably as MySQL relational tables.

## How this will help the research community

By transforming this data source to a more usable format and documenting the structure of the data in a way that is accessible to a wider audience of researchers and public interest programmers/techies, we will be making this public data accessible in a way that allows for efficient use in all sorts of social and public interest research projects. We are not the only organization that would directly and immediately benefit from this work. It appears the website http://mncriminals.com/ has already cracked this nut for their website, as have countless pay-for-access databases.

## Disclaimer

Please note: The data and source code contained herewithin are provided "AS-IS" and without warranty. We can't verify or gaurantee any of this information. Information may be out-of-date or otherwise innacurate. We are not responsible for misuse of this data. Don't use this data for anything other than the project outlined in "Project context" unless you have obtained it directly from the BCA.

The information here is provided for the sole purposes of writing code to translate this data source as described in the project context section. Please do not re-distribute this data source or reuse it for any other purposes at this time. If you would like obtain this data for other projects, please email me to get information on how you can obtain it directly from the BCA.

## BCA Disclaimers

These are verbatim disclosures of note contained on the DVD-ROM documentation from the BCA.

"It is your responsibility to assure proper use of this data in accordance with applicable state and federal law.  Please be advised that your improper use, retention or dissemination of this data may result in liability for you and/or your company/entity.  Such liability may include, specifically but not exclusively, violations of the Fair Credit Reporting Act, 15 U.S.C. §§ 1681-81t, as well as civil lawsuits under state or federal law."

"The criminal history files at the BCA are continually updated adding new data, modifying data, and removing data when so ordered by the courts.  In addition, because state law (MSS 13.87, subd. 2) states that the data are only public for 15 years following discharge from the sentence imposed, some of the data included herein will revert to private status and should not be used."