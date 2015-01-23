#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (medicationadministration.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import quantity
import ratio


class MedicationAdministration(fhirresource.FHIRResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_name = "MedicationAdministration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.effectiveTimeDateTime = None
        """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectiveTimePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ What was administered?.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who received medication?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Who administered substance?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationPrescription` (represented as `dict` in JSON). """
        
        self.reasonGiven = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | on hold | completed | entered in error | stopped.
        Type `str`. """
        
        self.wasNotGiven = False
        """ True if medication not administered.
        Type `bool`. """
        
        super(MedicationAdministration, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationAdministration, self).update_with_json(jsondict)
        if 'device' in jsondict:
            self.device = fhirreference.FHIRReference.with_json_and_owner(jsondict['device'], self)
        if 'dosage' in jsondict:
            self.dosage = MedicationAdministrationDosage.with_json_and_owner(jsondict['dosage'], self)
        if 'effectiveTimeDateTime' in jsondict:
            self.effectiveTimeDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['effectiveTimeDateTime'], self)
        if 'effectiveTimePeriod' in jsondict:
            self.effectiveTimePeriod = period.Period.with_json_and_owner(jsondict['effectiveTimePeriod'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'practitioner' in jsondict:
            self.practitioner = fhirreference.FHIRReference.with_json_and_owner(jsondict['practitioner'], self)
        if 'prescription' in jsondict:
            self.prescription = fhirreference.FHIRReference.with_json_and_owner(jsondict['prescription'], self)
        if 'reasonGiven' in jsondict:
            self.reasonGiven = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonGiven'], self)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonNotGiven'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']


class MedicationAdministrationDosage(fhirelement.FHIRElement):
    """ Details of how medication was taken.
    
    Indicates how the medication is/was used by the patient.
    """
    
    resource_name = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount administered in one dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage Instructions.
        Type `str`. """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationAdministrationDosage, self).update_with_json(jsondict)
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'rate' in jsondict:
            self.rate = ratio.Ratio.with_json_and_owner(jsondict['rate'], self)
        if 'route' in jsondict:
            self.route = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['route'], self)
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']

