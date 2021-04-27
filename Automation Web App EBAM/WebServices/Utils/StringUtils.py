def AddComment(query , dashboard_info):
    final ="/*  DashboardId  : " + str(dashboard_info['ID']) + "\n"
    final = final + "   Caption      : " + str(dashboard_info['Caption']) + "\n"
    final = final + "   Contact      : " + str(dashboard_info['Contact']) + "\n"
    final = final + "   ContactEmail : " + str(dashboard_info['ContactEmail']) + "\n"
    final = final + "   Creator      : " + str(dashboard_info['Creator']) + "\n"
    final = final + "   CreatorEmail : " + str(dashboard_info['CreatorEmail']) + "\n"
    final = final + " */" + "\n\n"
    return final + query