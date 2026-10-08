/** @odoo-module */
import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";

export class PropertyManagementDashboard extends Component {
    static template = "property_management.Dashboard";

    setup() {
        this.action = useService("action");

        this.state = useState({
            propertyCount: 0,
            soldCount: 0,
            maintenancePropertyCount: 0,
            requestCount: 0,
        });

        onWillStart(async () => {
            await this.loadDashboardData();
        });
    }

    async loadDashboardData() {
        this.state.propertyCount = await rpc("/web/dataset/call_kw", {
            model: "property.management",
            method: "search_count",
            args: [[]],
            kwargs: {},
        });

        this.state.soldCount = await rpc("/web/dataset/call_kw", {
            model: "property",
            method: "search_count",
            args: [[["state", "=", "sold"]]],
            kwargs: {},
        });

        this.state.maintenancePropertyCount = await rpc("/web/dataset/call_kw", {
            model: "maintenance.management",
            method: "search_count",
            args: [[]],
            kwargs: {},
        });

        this.state.requestCount = await rpc("/web/dataset/call_kw", {
            model: "home.request",
            method: "search_count",
            args: [[]],
            kwargs: {},
        });
    }

    openRealEstate() {
        this.action.doAction("property_management.property_management_action");
    }

    openMaintenance() {
        this.action.doAction("property_management.maintenance_management_action");
    }
}

registry.category("actions").add(
    "property_management.dashboard",
    PropertyManagementDashboard
);