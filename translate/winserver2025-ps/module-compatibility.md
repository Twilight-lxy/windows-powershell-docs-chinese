---
description: 本文列出了PowerShell 7的状态以及为其他Microsoft产品发布的PowerShell模块。  
ms.date: 02/07/2024
title: PowerShell 7模块在Windows Server 2025中的兼容性
---
# Windows Server 2025 中 PowerShell 7 模块的兼容性

本文列出了由微软发布的 PowerShell 模块。这些模块用于管理和支持微软的各种产品和服务。它们已经过更新，可以与 PowerShell 7 无缝配合使用；或者已经过兼容性测试，确保能够与 PowerShell 7 兼容。随着更多模块的被发现和测试，该列表将会持续更新，以包含最新的信息。

如果您有需要分享的信息，或者对某些特定模块存在疑问，请通过 Windows Feedback Hub 提交反馈。如需了解更多信息，请参阅[Send feedback to Microsoft with the Feedback Hub app][06]。

## Windows管理模块

Windows的管理模块的安装方式因 Windows 的版本以及该模块针对相应版本的打包方式而有所不同。

在 Windows Server 上，您需要以管理员身份使用 [Install-WindowsFeature][05] cmdlet 来安装相应的功能。例如：

```powershell
Install-WindowsFeature -Name ActiveDirectory
```

在 Windows 10 中，Windows 的管理模块被归类为 **Windows 可选功能（Windows Optional Features）**或**Windows 功能（Windows Capabilities）**。以下命令必须通过以管理员身份运行的 elevated 会话来执行。

- 对于Windows可选功能

  要获取可选功能的列表，请运行以下命令：

  ```powershell
  Get-WindowsOptionalFeature -Online
  ```

  要安装此功能：

  ```powershell
  Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-PowerShell
  ```

  有关更多信息，请参阅：

  - [Get-WindowsOptionalFeature][04]
  - [Enable-WindowsOptionalFeature][02]
- 适用于Windows功能

  要获取 Windows 功能列表，请运行以下命令：

  ```powershell
  Get-Windowscapability -online
  ```

  请注意，该功能包的名称以 `~~~~0.0.1.0` 结尾。您必须使用全名。
  安装该功能:

  ```powershell
  Add-WindowsCapability -Online -Name Rsat.ServerManager.Tools~~~~0.0.1.0
  ```

  有关更多信息，请参阅:

  - [Get-WindowsCapability][03]
  - [Add-WindowsCapability][01]

### 模块列表

| 模块名称                           | 状态                                 | 支持的操作系统                                                                                                        |
| ---------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| ActiveDirectory                    | Natively Compatible                  | Windows Server 1809+ with RSAT-AD-PowerShell<br />Windows 10 1809+ with Rsat.ActiveDirectory.DS-LDS.Tools             |
| ADDSDeployment                     | Works with Compatibility Layer       | Windows Server 2019 1809+                                                                                             |
| ADFS                               | Untested with Compatibility Layer    |                                                                                                                       |
| AppBackgroundTask                  | Natively Compatible                  | Windows 10 1903+                                                                                                      |
| AppLocker                          | Untested with Compatibility Layer    |                                                                                                                       |
| AppvClient                         | Untested with Compatibility Layer    |                                                                                                                       |
| Appx                               | Natively Compatible**                | Windows Server 1809+<br />Windows 10 1809+<br />**Must use Compatibility Layer with PowerShell 7.1                    |
| AssignedAccess                     | Natively Compatible                  | Windows 10 1809+                                                                                                      |
| BestPractices                      | Not Supported by Compatibility Layer |                                                                                                                       |
| BitLocker                          | Natively Compatible                  | Windows Server 1809+ with BitLocker<br />Windows 10 1809+                                                             |
| BitsTransfer                       | Natively Compatible                  | Windows Server 20H1<br />Windows 10 20H1                                                                              |
| BootEventCollector                 | Untested with Compatibility Layer    |                                                                                                                       |
| BranchCache                        | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| CimCmdlets                         | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| ClusterAwareUpdating               | Untested with Compatibility Layer    |                                                                                                                       |
| ConfigCI                           | Untested with Compatibility Layer    |                                                                                                                       |
| Defender                           | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| DeliveryOptimization               | Natively Compatible                  | Windows Server 1903+<br />Windows 10 1903+                                                                            |
| DFSN                               | Natively Compatible                  | Windows Server 1809+ with FS-DFS-Namespace<br />Windows 10 1809+ with Rsat.FailoverCluster.Management.Tools           |
| DFSR                               | Untested with Compatibility Layer    |                                                                                                                       |
| DhcpServer                         | Untested with Compatibility Layer    |                                                                                                                       |
| DirectAccessClientComponents       | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| Dism                               | Natively Compatible                  | Windows Server 1903+<br />Windows 10 1903+                                                                            |
| DnsClient                          | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| DnsServer                          | Natively Compatible                  | Windows Server 1809+ with DNS or RSAT-DNS-Server<br />Windows 10 1809+ with Rsat.Dns.Tools                            |
| EventTracingManagement             | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| FailoverClusters                   | Untested with Compatibility Layer    |                                                                                                                       |
| FailoverClusterSet                 | Untested with Compatibility Layer    |                                                                                                                       |
| FileServerResourceManager          | Natively Compatible                  | Windows Server 1809+ with FS-Resource-Manager                                                                         |
| GroupPolicy                        | Untested with Compatibility Layer    |                                                                                                                       |
| HgsClient                          | Natively Compatible                  | Windows Server 1903+ with Hyper-V or RSAT-Shielded-VM-Tools<br />Windows 10 1903+ with Rsat.Shielded.VM.Tools         |
| HgsDiagnostics                     | Natively Compatible                  | Windows Server 1809+ with Hyper-V or RSAT-Shielded-VM-Tools<br />Windows 10 1809+ with Rsat.Shielded.VM.Tools         |
| Hyper-V                            | Natively Compatible                  | Windows Server 1809+ with Hyper-V-PowerShell<br />Windows 10 1809+ with Microsoft-Hyper-V-Management-PowerShell       |
| IISAdministration                  | Untested with Compatibility Layer    |                                                                                                                       |
| International                      | Natively Compatible                  | Windows Server 1903+<br />Windows 10 1903+                                                                            |
| IpamServer                         | Untested with Compatibility Layer    |                                                                                                                       |
| iSCSI                              | Untested with Compatibility Layer    |                                                                                                                       |
| IscsiTarget                        | Untested with Compatibility Layer    |                                                                                                                       |
| ISE                                | Untested with Compatibility Layer    |                                                                                                                       |
| Kds                                | Natively Compatible                  | Windows Server 20H1<br />Windows 10 20H1                                                                              |
| Microsoft.PowerShell.Archive       | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.PowerShell.Diagnostics   | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.PowerShell.Host          | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.PowerShell.LocalAccounts | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| Microsoft.PowerShell.Management    | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.PowerShell.ODataUtils    | Untested with Compatibility Layer    |                                                                                                                       |
| Microsoft.PowerShell.Security      | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.PowerShell.Utility       | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| Microsoft.WSMan.Management         | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| MMAgent                            | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| MPIO                               | Natively Compatible                  | Windows Server 1809+ with Multipath-IO                                                                                |
| MsDtc                              | Untested with Compatibility Layer    |                                                                                                                       |
| NetAdapter                         | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetConnection                      | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetEventPacketCapture              | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetLbfo                            | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetLldpAgent                       | Untested with Compatibility Layer    |                                                                                                                       |
| NetNat                             | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetQos                             | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetSecurity                        | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetSwitchTeam                      | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetTCPIP                           | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetWNV                             | Untested with Compatibility Layer    |                                                                                                                       |
| NetworkConnectivityStatus          | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetworkController                  | Untested with Compatibility Layer    |                                                                                                                       |
| NetworkControllerDiagnostics       | Untested with Compatibility Layer    |                                                                                                                       |
| NetworkLoadBalancingClusters       | Untested with Compatibility Layer    |                                                                                                                       |
| NetworkSwitchManager               | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NetworkTransition                  | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| NFS                                | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+ with Rsat.ServerManager.Tools                                              |
| PackageManagement                  | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| PcsvDevice                         | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| PersistentMemory                   | Untested with Compatibility Layer    |                                                                                                                       |
| PKI                                | Untested with Compatibility Layer    |                                                                                                                       |
| PnpDevice                          | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| PowerShellGet                      | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| PrintManagement                    | Natively Compatible                  | Windows Server 1903+ with Print-Services<br />Windows 10 1903+                                                        |
| ProcessMitigations                 | Natively Compatible                  | Windows Server 1903+<br />Windows 10 1903+                                                                            |
| Provisioning                       | Untested with Compatibility Layer    |                                                                                                                       |
| PSDesiredStateConfiguration        | Partially                            | Built into PowerShell 7                                                                                               |
| PSDiagnostics                      | Natively Compatible                  | Built into PowerShell 7                                                                                               |
| PSScheduledJob                     | Not Supported by Compatibility Layer | Built into PowerShell 5.1                                                                                             |
| PSWorkflow                         | Untested with Compatibility Layer    |                                                                                                                       |
| PSWorkflowUtility                  | Untested with Compatibility Layer    |                                                                                                                       |
| RemoteAccess                       | Untested with Compatibility Layer    |                                                                                                                       |
| RemoteDesktop                      | Untested with Compatibility Layer    |                                                                                                                       |
| ScheduledTasks                     | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| SecureBoot                         | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| ServerCore                         | Untested with Compatibility Layer    |                                                                                                                       |
| ServerManager                      | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+ with Rsat.ServerManager.Tools <br />_See notes below_                    |
| ServerManagerTasks                 | Untested with Compatibility Layer    |                                                                                                                       |
| ShieldedVMDataFile                 | Natively Compatible                  | Windows Server 1903+ with RSAT-Shielded-VM-Tools<br />Windows 10 1903+ with Rsat.Shielded.VM.Tools                    |
| ShieldedVMProvisioning             | Natively Compatible                  | Windows Server 1809+ with HostGuardian<br />Windows 10 1809+ with HostGuardian                                        |
| ShieldedVMTemplate                 | Natively Compatible                  | Windows Server 1809+ with RSAT-Shielded-VM-Tools<br />Windows 10 1809+ with Rsat.Shielded.VM.Tools                    |
| SmbShare                           | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| SmbWitness                         | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| SMISConfig                         | Natively Compatible                  | Windows Server 1903+ with WindowsStorageManagementService                                                             |
| SMS                                | Untested with Compatibility Layer    |                                                                                                                       |
| SoftwareInventoryLogging           | Natively Compatible                  | Windows Server 1809+                                                                                                  |
| StartLayout                        | Natively Compatible                  | Windows Server 1809+ with Desktop Experience<br />Windows 10 1809+                                                    |
| Storage                            | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| StorageBusCache                    | Untested with Compatibility Layer    |                                                                                                                       |
| StorageMigrationService            | Untested with Compatibility Layer    |                                                                                                                       |
| StorageQOS                         | Natively Compatible                  | Windows Server 1809+ with RSAT-Clustering-PowerShell<br />Windows 10 1809+ with Rsat.FailoverCluster.Management.Tools |
| StorageReplica                     | Untested with Compatibility Layer    |                                                                                                                       |
| SyncShare                          | Natively Compatible                  | Windows Server 1809+ with FS-SyncShareService                                                                         |
| SystemInsights                     | Untested with Compatibility Layer    |                                                                                                                       |
| TLS                                | Untested with Compatibility Layer    |                                                                                                                       |
| TroubleshootingPack                | Natively Compatible                  | Windows 10 1903+                                                                                                      |
| TrustedPlatformModule              | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| UEV                                | Natively Compatible                  | Windows Server ??Future version of Server with Desktop Experience??<br />Windows 10 1903+                             |
| UpdateServices                     | Not Supported by Compatibility Layer |                                                                                                                       |
| VpnClient                          | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| Wdac                               | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| WebAdministration                  | Untested with Compatibility Layer    |                                                                                                                       |
| WHEA                               | Natively Compatible                  | Windows Server 1903+<br />Windows 10 1903+                                                                            |
| WindowsDeveloperLicense            | Natively Compatible                  | Windows Server 1809+ with Desktop Experience<br />Windows 10 1809+                                                    |
| WindowsErrorReporting              | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| WindowsSearch                      | Natively Compatible                  | Windows 10 1903+                                                                                                      |
| WindowsServerBackup                | Natively Compatible                  | Windows Server 19H2 with Windows-Server-Backup                                                                        |
| WindowsUpdate                      | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |
| WindowsUpdateProvider              | Natively Compatible                  | Windows Server 1809+<br />Windows 10 1809+                                                                            |

## 备注

### ServerManager 模块

该模块在 PowerShell 7 中存在一些与格式化输出相关的小问题。例如，`Get-WindowsFeature` cmdlet 可以返回包含所有属性的完整对象，但由于默认显示格式的原因，某些属性看起来是空的；实际上这些属性的值可以通过 `Select-Object` 或直接访问对象的成员来获取。

<!-- link references -->

[01]: /powershell/module/dism/add-windows Capability
[02]: /powershell/module/dism/enable-windowsoptionalfeature
[03]: /powershell/module/dism/get-windowss capability
[04]: /powershell/module/dism/get-windowsoptionalfeature
[05]: /powershell/module/servermanager/install-windowsfeature
[06]: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
