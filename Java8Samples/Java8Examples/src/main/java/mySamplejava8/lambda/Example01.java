package mySamplejava8.lambda;

public class Example01 {

	public static void main(String args[]) {
				
		IVehicle vehicle01=(VehicleDetails dtl1) -> {			
			return String.format("Make %s, Company Name %s ,Price %d", dtl1.getModel(),dtl1.getCompanyName(),dtl1.getPrice());		
				
		};
		
		String details1=vehicle01.getDetails(new VehicleDetails(2000000,"Make1","Company1"));
		System.out.print(details1);
	}
}
