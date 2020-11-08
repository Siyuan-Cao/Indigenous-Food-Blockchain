package com.example.demo;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Product {
    private String productID;
    private String productName;
    private String productBrand;
    private String productLocation;
    private String productOwner;

    public Product(@JsonProperty("id") String productID, @JsonProperty("name") String productName,
            @JsonProperty("brand") String productBrand, @JsonProperty("location") String productLocation,
            @JsonProperty("owner") String productOwner) {
        this.productID = productID;
        this.productName = productName;
        this.productBrand = productBrand;
        this.productLocation = productLocation;
        this.productOwner = productOwner;
    }

    public String getProductID() {
        return productID;
    }

    public void setProductID(String productID) {
        this.productID = productID;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public String getProductBrand() {
        return productBrand;
    }

    public void setProductBrand(String productBrand) {
        this.productBrand = productBrand;
    }

    public String getProductLocation() {
        return productLocation;
    }

    public void setProductLocation(String productLocation) {
        this.productLocation = productLocation;
    }

    public String getProductOwner() {
        return productOwner;
    }

    public void setProductOwner(String productOwner) {
        this.productOwner = productOwner;
    }
}
