class DHLResponse:
    def __init__(self, success, errors=None):
        self.success = success
        self.errors = errors

    def __str__(self):
        return '%s' % ('Success' if self.success else 'Fail: '+str(self.errors))


class DHLRateResponse(DHLResponse):
    def __init__(self, success, services, errors=None):
        DHLResponse.__init__(self, success, errors)
        list_services = []
        for service in services:
            service_dict = {
                'type': service._type,
                'total_net': {
                    'currency': service.TotalNet.Currency,
                    'amount': service.TotalNet.Amount
                },
                'charges': [],
                'delivery_time': service.DeliveryTime,
                'cutoff_time': service.CutoffTime,
                'next_business_day_ind': service.NextBusinessDayInd
            }
            for charge in service.Charges.Charge:
                service_dict['charges'].append({
                    'currency': service.Charges.Currency,
                    'charge_type': charge.ChargeType,
                    'charge_amount': charge.ChargeAmount
                })
            list_services.append(service_dict)
        self.services = list_services


class DHLShipmentResponse(DHLResponse):
    def __init__(self, success, tracking_numbers=None, identification_number=None, dispatch_number=None,
                 label_bytes=None, errors=None):
        DHLResponse.__init__(self, success, errors)

        self.tracking_numbers = tracking_numbers
        self.identification_number = identification_number
        self.dispatch_number = dispatch_number
        self.label_bytes = label_bytes


class DHLTrackingResponse(DHLResponse):
    def __init__(self, success, shipment_events=None, pieces_events=None, errors=None):
        DHLResponse.__init__(self, success, errors)

        self.shipment_events = shipment_events  # DHLTackingEvent
        self.pieces_events = pieces_events  # {tracking : [DHLTackingEvent...] ... }



class DHLPodResponse(DHLResponse):
    def __init__(self, success, pod_bytes=None, errors=None):
        DHLResponse.__init__(self, success, errors)

        self.pod_bytes = pod_bytes


class DHLTrackingEvent:
    def __init__(self, code=None, description=None, location_code=None, location_description=None, date=None,
                 time=None):
        self.date = date
        self.time = time
        self.code = code
        self.description = description
        self.location_code = location_code
        self.location_description = location_description
