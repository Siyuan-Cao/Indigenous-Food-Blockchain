package com.example.demo;

/*
SPDX-License-Identifier: Apache-2.0
*/

import java.nio.file.Path;
import java.nio.file.Paths;

import com.fasterxml.jackson.annotation.JsonProperty;

import org.hyperledger.fabric.gateway.Contract;
import org.hyperledger.fabric.gateway.ContractException;
import org.hyperledger.fabric.gateway.Gateway;
import org.hyperledger.fabric.gateway.Network;
import org.hyperledger.fabric.gateway.Wallet;
import org.hyperledger.fabric.gateway.Wallets;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("api/v1/client")
@RestController
public class ClientApp {
	byte[] result;
	static {
		System.setProperty("org.hyperledger.fabric.sdk.service_discovery.as_localhost", "true");
	}

	public static void main(String[] args) throws Exception {
		// Load a file system based wallet for managing identities.
		Path walletPath = Paths.get("wallet");
		Wallet wallet = Wallets.newFileSystemWallet(walletPath);
		// load a CCP
		Path networkConfigPath = Paths.get("..", "Backend", "test-network", "organizations", "peerOrganizations",
				"org1.example.com", "connection-org1.yaml");

		Gateway.Builder builder = Gateway.createBuilder();
		builder.identity(wallet, "appUser").networkConfig(networkConfigPath).discovery(true);
	}

	public Gateway.Builder getBuilder() throws Exception {
		// Load a file system based wallet for managing identities.
		Path walletPath = Paths.get("wallet");
		Wallet wallet = Wallets.newFileSystemWallet(walletPath);
		// load a CCP
		Path networkConfigPath = Paths.get("..", "Backend", "test-network", "organizations", "peerOrganizations",
				"org1.example.com", "connection-org1.yaml");

		Gateway.Builder builder = Gateway.createBuilder();
		builder.identity(wallet, "appUser").networkConfig(networkConfigPath).discovery(true);
		return builder;
	}

	@GetMapping
	public byte[] queryAll() throws Exception {
		try (Gateway gateway = getBuilder().connect()) {
			Network network = gateway.getNetwork("mychannel");
			Contract contract = network.getContract("foodchain");
			result = contract.evaluateTransaction("queryAllProducts");
		}
		return result;
	}

	@PostMapping
	public void addProduct(@RequestBody Product product) throws Exception {
		try (Gateway gateway = getBuilder().connect()) {
			Network network = gateway.getNetwork("mychannel");
			Contract contract = network.getContract("foodchain");
			contract.submitTransaction("createProduct", product.getProductID(), product.getProductName(), product.getProductBrand(), product.getProductLocation(), product.getProductOwner());
		}
	}

	@PostMapping(path = "update")
	public void updateProduct(@RequestBody Product product) throws Exception {
		try (Gateway gateway = getBuilder().connect()) {
			Network network = gateway.getNetwork("mychannel");
			Contract contract = network.getContract("foodchain");
			contract.submitTransaction("updateProduct", product.getProductID(), product.getProductName(), product.getProductBrand(), product.getProductLocation(), product.getProductOwner());
		}
	}

	@GetMapping(path = "{id}")
	public byte[] queryProduct(@PathVariable("id") String productNumber) throws Exception {
		try (Gateway gateway = getBuilder().connect()) {
			Network network = gateway.getNetwork("mychannel");
			Contract contract = network.getContract("foodchain");
			result = contract.submitTransaction("queryProduct", productNumber);
		}
		return result;
	}
}
