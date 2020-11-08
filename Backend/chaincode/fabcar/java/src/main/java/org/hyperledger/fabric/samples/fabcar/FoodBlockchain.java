/*
 * SPDX-License-Identifier: Apache-2.0
 */

package org.hyperledger.fabric.samples.fabcar;

import java.util.ArrayList;
import java.util.List;

import org.hyperledger.fabric.contract.Context;
import org.hyperledger.fabric.contract.ContractInterface;
import org.hyperledger.fabric.contract.annotation.Contact;
import org.hyperledger.fabric.contract.annotation.Contract;
import org.hyperledger.fabric.contract.annotation.Default;
import org.hyperledger.fabric.contract.annotation.Info;
import org.hyperledger.fabric.contract.annotation.License;
import org.hyperledger.fabric.contract.annotation.Transaction;
import org.hyperledger.fabric.shim.ChaincodeException;
import org.hyperledger.fabric.shim.ChaincodeStub;
import org.hyperledger.fabric.shim.ledger.KeyValue;
import org.hyperledger.fabric.shim.ledger.QueryResultsIterator;

import com.owlike.genson.Genson;

/**
 * Java implementation of the Fabric product Contract
 */
@Contract(name = "FoodBlockchain", info = @Info(title = "FoodBlockchain contract", description = "FoodBlockchain contract", version = "0.0.1-SNAPSHOT", license = @License(name = "Apache 2.0 License", url = "http://www.apache.org/licenses/LICENSE-2.0.html"), contact = @Contact(email = "rmit@example.com", name = "R Mit", url = "https://hyperledger.example.com")))
@Default
public final class FoodBlockchain implements ContractInterface {

    private final Genson genson = new Genson();

    private enum FoodBlockchainErrors {
        PRODUCT_NOT_FOUND, PRODUCT_ALREADY_EXISTS
    }

    /**
     * Creates some initial products on the ledger.
     *
     * @param ctx the transaction context
     */
    @Transaction()
    public void initLedger(final Context ctx) {
        ChaincodeStub stub = ctx.getStub();

        String[] productData = {
                "{ \"name\": \"Apple\", \"brand\": \"Red Apple\", \"location\": \"Dandenong\", \"owner\": \"RMIT\" }",
                "{ \"name\": \"Pear\", \"brand\": \"Green Pear\", \"location\": \"Mel\", \"owner\": \"Blockchain\" }" };

        for (int i = 0; i < productData.length; i++) {
            String key = String.format("P%d", i);

            Product product = genson.deserialize(productData[i], Product.class);
            String chainState = genson.serialize(product);
            stub.putStringState(key, chainState);
        }
    }

    /**
     * Creates a new product on the ledger.
     *
     * @param ctx      the transaction context
     * @param key      the key for the new product
     * @param name     the name of the new product
     * @param brand    the brand of the new product
     * @param location the location of the new product
     * @param owner    the owner of the new product
     * @return the created Product
     */
    @Transaction()
    public Product createProduct(final Context ctx, final String key, final String name, final String brand,
            final String location, final String owner) {
        ChaincodeStub stub = ctx.getStub();

        String chainState = stub.getStringState(key);
        if (!chainState.isEmpty()) {
            String errorMessage = String.format("Product %s already exists", key);
            System.out.println(errorMessage);
            throw new ChaincodeException(errorMessage, FoodBlockchainErrors.PRODUCT_ALREADY_EXISTS.toString());
        }

        Product product = new Product(name, brand, location, owner);
        chainState = genson.serialize(product);
        stub.putStringState(key, chainState);

        return product;
    }

    /**
     * Retrieves a product with the specified key from the ledger.
     *
     * @param ctx the transaction context
     * @param key the key
     * @return the product found on the ledger if there was one
     */
    @Transaction()
    public Product queryProduct(final Context ctx, final String key) {
        ChaincodeStub stub = ctx.getStub();
        String chainState = stub.getStringState(key);

        if (chainState.isEmpty()) {
            String errorMessage = String.format("Product %s does not exist", key);
            System.out.println(errorMessage);
            throw new ChaincodeException(errorMessage, FoodBlockchainErrors.PRODUCT_NOT_FOUND.toString());
        }

        Product product = genson.deserialize(chainState, Product.class);

        return product;
    }

    /**
     * Retrieves all products from the ledger.
     *
     * @param ctx the transaction context
     * @return array of products found on the ledger
     */
    @Transaction()
    public String queryAllProducts(final Context ctx) {
        ChaincodeStub stub = ctx.getStub();

        final String startKey = "P0";
        final String endKey = "P99";
        List<ProductQueryResult> queryResults = new ArrayList<ProductQueryResult>();

        QueryResultsIterator<KeyValue> results = stub.getStateByRange(startKey, endKey);

        for (KeyValue result : results) {
            Product product = genson.deserialize(result.getStringValue(), Product.class);
            queryResults.add(new ProductQueryResult(result.getKey(), product));
        }

        final String response = genson.serialize(queryResults);

        return response;
    }

    /**
     * Changes the owner of a product on the ledger.
     *
     * @param ctx      the transaction context
     * @param key      the key
     * @param newOwner the new owner
     * @return the updated product
     */
    @Transaction()
    public Product changeProductOwner(final Context ctx, final String key, final String newOwner) {
        ChaincodeStub stub = ctx.getStub();

        String chainState = stub.getStringState(key);

        if (chainState.isEmpty()) {
            String errorMessage = String.format("Product %s does not exist", key);
            System.out.println(errorMessage);
            throw new ChaincodeException(errorMessage, FoodBlockchainErrors.PRODUCT_NOT_FOUND.toString());
        }

        Product product = genson.deserialize(chainState, Product.class);

        Product newProduct = new Product(product.getName(), product.getBrand(), product.getLocation(), newOwner);
        String newProductState = genson.serialize(newProduct);
        stub.putStringState(key, newProductState);

        return newProduct;
    }

    /**
     * Update a  product on the ledger.
     *
     * @param ctx      the transaction context
     * @param key      the key for the new product
     * @param name     the name of the new product
     * @param brand    the brand of the new product
     * @param location the location of the new product
     * @param owner    the owner of the new product
     * @return the created Product
     */
    @Transaction()
    public Product updateProduct(final Context ctx, final String key, final String newName, final String newBrand,
            final String newLocation, final String newOwner) {

        ChaincodeStub stub = ctx.getStub();

        String chainState = stub.getStringState(key);

        if (chainState.isEmpty()) {
            String errorMessage = String.format("Product %s does not exist", key);
            System.out.println(errorMessage);
            throw new ChaincodeException(errorMessage, FoodBlockchainErrors.PRODUCT_NOT_FOUND.toString());
        }

        //Product product = genson.deserialize(chainState, Product.class);
        Product newProduct = new Product(newName, newBrand, newLocation, newOwner);
        String newProductState = genson.serialize(newProduct);
        stub.putStringState(key, newProductState);

        return newProduct;
    }
}
