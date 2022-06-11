package mySamplejava8.lambda;

public class VehicleDetails {
	private int price;
	private String model;
	private String companyName;
	public VehicleDetails(int price,String model,String companyName) {
		this.model=model;
		this.companyName=companyName;
		this.price=price;
		
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	public String getCompanyName() {
		return companyName;
	}
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}

}
