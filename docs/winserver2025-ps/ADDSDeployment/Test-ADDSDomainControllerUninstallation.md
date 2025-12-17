---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/test-addsdomaincontrolleruninstallation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ADDSDomainControllerUninstallation
---

# 测试 ADDSDomainController 的卸载功能

## 摘要
运行用于卸载 Active Directory 中域控制器所需的先决条件程序。

## 语法

### ADDSDomainControllerUninstall（默认值）

```
Test-ADDSDomainControllerUninstallation [-LocalAdministratorPassword <SecureString>]
 [-Credential <PSCredential>] [-DemoteOperationMasterRole]
 [-DnsDelegationRemovalCredential <PSCredential>] [-IgnoreLastDCInDomainMismatch]
 [-IgnoreLastDnsServerForZone] [-LastDomainControllerInDomain] [-NoRebootOnCompletion]
 [-RemoveApplicationPartitions] [-RemoveDnsDelegation] [-RetainDCMetadata] [-Force]
 [<CommonParameters>]
```

### ADDSDomainControllerUninstallForceRemoval

```
Test-ADDSDomainControllerUninstallation [-LocalAdministratorPassword <SecureString>]
 [-Credential <PSCredential>] [-DemoteOperationMasterRole] [-ForceRemoval]
 [-NoRebootOnCompletion] [-Force] [<CommonParameters>]
```

## 描述

`Test-ADDSDomainControllerUninstallation` 这个 cmdlet 会执行那些先决条件检查，这些检查类似于当你使用 `Uninstall-ADDSDomainController` cmdlet 来卸载 Active Directory 中的域控制器时所进行的检查。它与使用 `Uninstall-ADDSDomainController` cmdlet 的 **WhatIf** 参数有所不同：该 cmdlet 不是总结卸载过程中将会发生的变化，而是实际测试在当前环境下这些变化是否可行。

有关 **ADDSDeployment** 模块在使用此 cmdlet 时执行的这些先决条件检查的范围的更多信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中的“ADPrep 和先决条件检查架构”部分。

## 示例

### 示例 1：测试是否可以卸载域控制器

```powershell
Test-ADDSDomainControllerUninstallation
```

此命令会运行相关预处理步骤，以确定是否可以在某个域中卸载额外的域控制器。在完成卸载过程之前，该命令还会提示用户设置并确认本地管理员密码。

## 参数

### -Credential

指定用于安装域控制器的账户的用户名和密码。如果要提示用户输入密码，可以使用 `Runs the prerequisites (only)` 命令来检查是否能够使用域管理员凭据安装包含 `corp.contoso.com` 域的 DNS 服务器的域控制器，并在之后提示用户正确输入目录服务恢复模式（DSRM）的密码。请使用 `Get-Credential` cmdlet 来代替现有的 **PSCredential** 类型。此参数会促使 Windows PowerShell 通过 Windows 安全登录界面来请求用户输入凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DemoteOperationMasterRole

这意味着即使从正在删除 AD DS 的域控制器上发现了操作主机（Operations Master）角色，强制降级操作仍应继续进行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DnsDelegationRemovalCredential

指定在创建或删除 DNS 委派时使用的账户凭据。如果您未指定任何值，则会使用为 AD DS 安装或删除操作指定的账户凭据来删除 DNS 委派。或者，您也可以使用星号（`*`）来提示用户输入凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceRemoval

表示该cmdlet会强制删除域控制器。如果您需要删除某个域控制器，但无法与域拓扑中的其他域控制器建立连接，可以使用此参数来强制卸载AD DS。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstallForceRemoval
Aliases:

Required: True
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreLastDCInDomainMismatch

这表示 Windows PowerShell 会忽略其在 **LastDomainControllerInDomain** 参数所指定的值与实际情况之间的任何不一致之处。例如，如果您指定了 **LastDomainControllerInDomain**，但 Windows PowerShell 发现该域中实际上还有另一个活动中的域控制器，您可以指定 **IgnoreLastDCInDomainMismatch** 参数，让 Windows PowerShell 尽管检测到这种不一致仍继续从该域控制器中移除 AD DS。同样地，如果您没有指定 **LastDomainControllerInDomain**，但 Windows PowerShell 无法确定该域中是否存在其他域控制器，您也可以指定 **IgnoreLastDCInDomainMismatch** 参数，以便 Windows PowerShell 继续执行从该域控制器中移除 AD DS 的操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreLastDnsServerForZone

这表示即使该域控制器是一个或多个由 Active Directory 集成的 DNS 区域的最后一个 DNS 服务器，该 cmdlet 仍会继续执行删除操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -LastDomainControllerInDomain

表示该cmdlet会从域中的最后一个控制器中删除AD DS（Active Directory Domain Services）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalAdministratorPassword

当从域控制器中删除 AD DS 时，该参数用于指定本地管理员账户的密码。在早期版本中，使用 `Dcpromo.exe` 来卸载 AD DS 以降低其角色（例如将其降级为普通域控制器）时，默认情况下允许此设置为空密码。但在 Windows PowerShell 中，ADDS Deployment 模块要求必须为其分配一个非空的密码字符串。如果未为此参数提供值，系统会提示您在 Windows PowerShell 提示符下输入密码。密码值必须是安全的（即不能包含容易被猜到的字符或信息）。

如果未指定此参数，cmdlet 会提示您输入并确认一个经过遮蔽处理的密码。这是交互式运行该 cmdlet 时的推荐用法。此外，如果没有为该 cmdlet 指定其他参数，系统也会提示您输入这个被遮蔽的密码，但不会对输入的密码进行任何确认。这种做法并不建议使用，因为可能会导致错误的密码被配置到系统中。另一种高级选项是使用 `ConvertTo-SecureString` cmdlet，并将密码字符串以未遮蔽的形式直接作为控制台输入来提供；然而，在生产环境中的部署中，这同样不是推荐的安全最佳实践。

```yaml
Type: System.Security.SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoRebootOnCompletion

该参数表示：无论命令是否成功执行，此cmdlet在完成操作后都不会重启计算机。默认情况下，当使用此cmdlet且省略该参数时，系统会在执行完成后自动重启。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoveApplicationPartitions

表示该cmdlet在从域控制器中删除AD DS时还会同时删除与该域控制器关联的应用程序分区。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoveDnsDelegation

表示该cmdlet会保留来自父DNS区域的、指向此DNS服务器的DNS委派（ delegation ）设置。

默认情况下，此参数被设置为 `$false`，这意味着当域控制器卸载后，来自父DNS区域的指向该服务器的DNS委托（delegations）将不会被保留。这个设置与早期的 `Dcpromo.exe` 命令行工具的默认参数 `/RemoveDNSDelegation:Yes` 是一致的。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetainDCMetadata

表示在删除 Active Directory Domain Services (AD DS) 之后，域控制器仍应保留该域的元数据。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[简化 AD DS 管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[卸载-ADDSDomainController](./Uninstall-ADDSDomainController.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
