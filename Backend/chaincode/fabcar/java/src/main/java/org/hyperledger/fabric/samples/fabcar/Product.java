/*
 * SPDX-License-Identifier: Apache-2.0
 */

package org.hyperledger.fabric.samples.fabcar;

import java.util.Objects;

import org.hyperledger.fabric.contract.annotation.DataType;
import org.hyperledger.fabric.contract.annotation.Property;

import com.owlike.genson.annotation.JsonProperty;

@DataType()
public final class Product {

    @Property()
    private final String name;

    @Property()
    private final String brand;

    @Property()
    private final String location;

    @Property()
    private final String owner;

    public String getName() {
        return name;
    }

    public String getBrand() {
        return brand;
    }

    public String getLocation() {
        return location;
    }

    public String getOwner() {
        return owner;
    }

    public Product(@JsonProperty("name") final String name, @JsonProperty("brand") final String brand,
            @JsonProperty("location") final String location, @JsonProperty("owner") final String owner) {
        this.name = name;
        this.brand = brand;
        this.location = location;
        this.owner = owner;
    }

    @Override
    public boolean equals(final Object obj) {
        if (this == obj) {
            return true;
        }

        if ((obj == null) || (getClass() != obj.getClass())) {
            return false;
        }

        Product other = (Product) obj;

        return Objects.deepEquals(new String[] {getName(), getBrand(), getLocation(), getOwner()},
                new String[] {other.getName(), other.getBrand(), other.getLocation(), other.getOwner()});
    }

    @Override
    public int hashCode() {
        return Objects.hash(getName(), getBrand(), getLocation(), getOwner());
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "@" + Integer.toHexString(hashCode()) + " [name=" + name + ", brand="
                + brand + ", location=" + location + ", owner=" + owner + "]";
    }
}
