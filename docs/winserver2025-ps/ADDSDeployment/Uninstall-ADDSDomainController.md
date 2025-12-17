---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/uninstall-addsdomaincontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-ADDSDomainController
---

# 卸载 ADDSDomainController

## 摘要
卸载Active Directory中的域控制器。

## 语法

### ADDSDomainControllerUninstall（默认值）

```
Uninstall-ADDSDomainController [-SkipPreChecks]
 [-LocalAdministratorPassword <SecureString>] [-Credential <PSCredential>]
 [-DemoteOperationMasterRole] [-DnsDelegationRemovalCredential <PSCredential>]
 [-IgnoreLastDCInDomainMismatch] [-IgnoreLastDnsServerForZone]
 [-LastDomainControllerInDomain] [-NoRebootOnCompletion] [-RemoveApplicationPartitions]
 [-RemoveDnsDelegation] [-RetainDCMetadata] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ADDSDomainControllerUninstallForceRemoval

```
Uninstall-ADDSDomainController [-SkipPreChecks]
 [-LocalAdministratorPassword <SecureString>]
 [-Credential <PSCredential>] [-DemoteOperationMasterRole] [-ForceRemoval]
 [-NoRebootOnCompletion] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Uninstall-ADDSDomainController` cmdlet 用于卸载 Active Directory 中的域控制器。

## 示例

### 示例 1：从域控制器中删除 AD DS（Active Directory Domain Services）

```powershell
Uninstall-ADDSDomainController
```

此命令用于从域中的另一个域控制器中删除 AD DS（Active Directory Domain Services）。在完成删除过程之前，系统会提示用户设置并确认本地管理员密码。

## 参数

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于安装域控制器的账户对应的用户名和密码。可以使用 `Get-Credential` cmdlet 来提示用户输入密码，而不是使用现有的 **System.Management Automation.PSCredential** 类型。这样，Windows PowerShell 会通过 Windows 安全登录界面来提示用户输入凭据。

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

这意味着即使从正在卸载 AD DS 的域控制器上发现了操作主机（Operation Master）角色，强制降级操作仍应继续进行。

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

指定在创建或删除 DNS 委派时使用的账户凭据。如果您没有指定值，则会使用为 AD DS 安装或删除操作指定的账户凭据来删除 DNS 委派。或者，您也可以指定星号（`*`），以提示用户输入凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: None
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

表示该cmdlet会强制删除某个域控制器。如果您需要删除该域控制器，但又无法与域拓扑结构中的其他域控制器建立连接，可以使用此参数来强制卸载AD DS。

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

这表示 Windows PowerShell 会忽略其检测到的与您为参数 **LastDomainControllerInDomain** 指定的值之间的任何不一致之处。例如，如果您指定了 **LastDomainControllerInDomain**，但 Windows PowerShell 发现该域中实际上还存在另一个活动域控制器，您可以指定参数 **IgnoreLastDCInDomainMismatch**，以便 Windows PowerShell 继续从该域控制器中删除 AD DS，而忽略检测到的不一致情况。同样地，如果您没有指定 **LastDomainControllerInDomain**，但 Windows PowerShell 无法确认该域中是否存在其他域控制器，您也可以指定参数 **IgnoreLastDCInDomainMismatch**，让 Windows PowerShell 继续执行从该域控制器中删除 AD DS 的操作。

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

这表示，即使该域控制器是一个或多个由 Active Directory 集成的 DNS 区域的最后一个 DNS 服务器，cmdlet 仍会继续执行删除操作。

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

### -LastDomainControllerInDomain

这表明正在卸载 AD DS 的计算机是该域中的最后一个域控制器。

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

当从域控制器中删除 AD DS 时，此参数用于指定本地管理员账户的密码。在早期版本中，使用 `Dcpromo.exe` 来卸载 AD DS 以降低其角色（即将其降级为普通域控制器）时，该设置的默认值为允许使用空密码。而在 Windows PowerShell 中，ADDS Deployment 模块要求必须为其指定一个非空的密码字符串值。如果未为此参数提供任何值，系统会在 Windows PowerShell 提示符下提示您输入密码。密码必须是一个安全的字符串。

如果未指定此参数，cmdlet 会提示您输入并确认一个经过加密处理的密码。这是交互式运行该 cmdlet 时的首选方式。此外，如果您没有为该 cmdlet 指定其他参数，系统也会提示您输入密码，但不会对输入的密码进行任何验证。这种做法并不推荐，因为这样可能会导致错误输入的密码被成功配置。另一个高级选项是使用 `ConvertTo-SecureString` cmdlet，并以未加密的形式直接在命令行中输入密码字符串；不过，在生产环境中，这同样不符合安全最佳实践。

```yaml
Type: System.Security.SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoRebootOnCompletion

该参数表示：无论操作是否成功，此 cmdlet 在执行完成后都会重启计算机。默认情况下，当使用此 cmdlet 且省略该参数时，系统会在执行完成后自动重启。微软支持团队一般建议不要使用该参数（除非用于测试或故障排除），因为配置完成之后，服务器在重新启动之前将无法正常作为成员服务器或域控制器（DC）运行。

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

### -RemoveApplicationPartitions

该命令行工具用于在从域控制器中删除 Active Directory Domain Services (AD DS) 时同时移除与该 AD DS 相关的应用程序分区。

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

该参数用于指定是否保留来自父DNS区域的指向此DNS服务器的DNS委托关系。如果使用此参数，则在卸载域控制器后，来自父DNS区域的指向该服务器的DNS委托关系将不会被保留。此设置与早期`Dcpromo.exe`命令行的默认参数`/RemoveDNSDelegation:Yes`相对应。

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

### -RetainDCMetadata

表示在卸载完成后应保留来自域控制器的元数据。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUninstall
Aliases:

Required: False
Position: Named
Default value: FALSE
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipPreChecks

这表示仅执行最基本的验证步骤。这种行为等同于在早期版本的 Windows Server 中使用 `Dcpromo.exe` 添加新的域控制器时所执行的验证过程。当设置此参数时，意味着应跳过额外的初步检查。有关 **ADDSDeployment** 模块在使用 Windows Server 2012 时默认执行的所有这些额外初步检查的详细信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中“ADPrep 和先决条件检查架构”部分中的表格。

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

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[简化 AD DS 管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[Install-ADDSDomainController](./Install-ADDSDomainController.md)

[获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
