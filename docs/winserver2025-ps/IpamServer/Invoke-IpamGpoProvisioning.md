---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamGpo.psm1-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/invoke-ipamgpoprovisioning?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-IpamGpoProvisioning
---

# 调用 IpamGpoProvisioning

## 摘要
在指定的域中创建并链接组策略，以便为运行IPAM服务器的计算机管理的服务器提供所需的访问设置。

## 语法

```
Invoke-IpamGpoProvisioning [-Domain] <String> [-GpoPrefixName] <String> [-IpamServerFqdn <String>]
 [-DelegatedGpoUser <String[]>] [-DelegatedGpoGroup <String[]>] [-DomainController <String>] [-PassThru]
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Invoke-IpamGpoProvisioning` cmdlet 会创建并链接三个组策略（这些组策略是在 `Domain` 参数中指定的），用于为由运行 IP 地址管理 (IPAM) 服务器的计算机所管理的服务器角色配置所需的访问设置。指定的 `GpoPrefixName` 参数应与 IPAM 配置向导中配置的前缀相同。这三个组策略对象（Group Policy Objects，简称 GPOs）会在 `GpoPrefixName` 的值后添加 `_DHCP`、`_DNS` 和 `_DC_NPS` 这三个后缀。这些后缀表示根据运行 IPAM 服务器的计算机所管理的服务器角色类型，这些组策略将分别用于配置三种不同类型的访问设置。

由创建的GPOs（组策略对象）传播的访问设置是定期IPAM数据收集任务所必需的，这些任务默认是在“Network Service”账户下运行的。这些访问设置会应用于运行IPAM服务器的计算机的账户上，因为“Network Service”账户使用的凭据就是用来访问远程资源的。如果需要，管理员可以使用**IpamServerFqdn**参数明确指定运行IPAM服务器的计算机的完全限定域名（FQDN）；如果没有指定，则默认使用“localhost”作为**IpamServerFqdn**的值。该cmdlet会在由**Domain**参数指定的域中创建一个名为IPAMUG的通用组；如果这个通用组已经存在，那么创建步骤将会被跳过。随后，该cmdlet会将由**IpamServerFqdn**参数指定的计算机账户添加到名为IPAMUG的通用组中。所有通过IPAM GPOs进行的访问设置传播操作都是针对名为IPAMUG的通用组来执行的。此外，该cmdlet还会修改整个域的DNS访问控制列表（ACL），以允许名为IPAMUG的通用组能够进行DNS远程过程调用（RPC）操作。

默认情况下，GPO（组策略对象）的创建是在指定域的PDC模拟器上完成的。可以通过使用`DomainController`参数来明确选择用于创建GPO的域控制器。使用此cmdlet创建的GPO可以通过`PassThru`参数返回。

在创建组策略对象（GPO）时，IPAM组策略对象的安全过滤列表是空的。当用户在IPAM服务器库存视图中编辑某台服务器的管理状态时，运行该IPAM服务器的计算机会自动将该服务器添加到相应的GPO安全过滤列表中（如果需要的话），或者从列表中删除它。被管理的服务器会被添加到GPO的安全过滤规则中，而未被管理的服务器则会被从列表中移除。

注意：此cmdlet需要具有域管理员权限才能创建组策略对象（GPO）。后续对IPAM GPO的编辑操作权限可以委托给非域管理员或非企业管理员的IPAM管理员，具体可以通过`DelegatedGpoUser`和`DelegatedGpoGroup`参数来实现。

## 示例

### 示例 1：配置组策略对象（GPOs）
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "child.contoso.com" -GpoPrefixName "IPAM1" -Force
```

此命令会在名为 `child.contoso.com` 的域中创建一个通用组 `IPAMUG`（如果该组还不存在的话），并将运行 IPAM 服务器的本地计算机的账户添加到该组中。该 cmdlet 会创建并链接以下 IPAM GPO（Group Policy Objects）：`IPAM1_DHCP`、`IPAM1_DNS` 和 `IPAM1_DC_NPS`，以便 `IPAMUG` 组能够访问这些资源。此外，该 cmdlet 还通过域范围内的 DNS 访问控制列表 (ACL) 为 `IPAMUG` 组启用 DNS 读取权限。由于没有明确指定域控制器，因此该 cmdlet 会与 PDC 模拟器（Primary Domain Controller emulator）进行通信以完成 GPO 操作。另外，该 cmdlet 会忽略默认的确认提示信息。

#### 示例 2：使用特定的域控制器来配置组策略对象（GPO）
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "child.contoso.com" -GpoPrefixName "IPAM1" -DomainController "dc1.child.contoso.com" -Force
```

此命令会在名为 child.contoso.com 的域中创建一个通用组 IPAMUG（如果该组还不存在的话），并将运行 IPAM 服务器的本地计算机的账户添加到该组中。此外，此 cmdlet 还会在该域中创建并链接以下 IPAM GPO（组策略对象）：IPAM1_DHCP、IPAM1_DNS 和 IPAM1_DC_NPS，以使 IPAMUG 组能够访问这些资源。通过使用全域范围内的 DNS 访问控制列表 (ACL)，此 cmdlet 为 IPAMUG 组启用了 DNS 读取权限。在执行 GPO 操作时，此 cmdlet 使用名为 dc1.child.contoso.com 的域控制器作为数据存储控制器 (DC)。同时，此 cmdlet 禁用了默认的确认提示信息。

### 示例 3：使用完全限定域名（FQDN）配置组策略对象（GPO）
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "child.contoso.com" -GpoPrefixName "IPAM2" -IpamServerFqdn "Ipam2.Contoso.com" -Force
```

此命令会创建一个名为 IPAMUG 的通用组（如果该组尚不存在的话），并将运行 IPAM 服务器（ipam2.contoso.com）的计算机账户添加到该组中。此外，该命令还会在 domain.child.contoso.com 域内创建并关联以下三个 IPAM GPO（Group Policy Objects）：IPAM2_DHCP、IPAM2_DNS 和 IPAM2_DC_NPS，以便使名为 IPAMUG 的通用组能够访问这些资源。同时，该命令通过域范围的 DNS 访问控制列表（Access Control List, ACL）为名为 IPAMUG 的通用组启用 DNS 读取权限。最后，该命令会屏蔽默认的确认提示信息。

### 示例 4：配置组策略对象（GPO）并授权用户使用该 GPO
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "child.contoso.com" -GpoPrefixName "IPAM1" -DelegatedGpoUser "NetworkAdmin1,NetworkAdmin2" -Force
```

此命令会在域 child.contoso.com 中创建一个名为 IPAMUG 的通用组（如果该组还不存在的话），并将运行 IPAM 服务器的本地计算机的账户添加到该组中。该 cmdlet 会在域 child.contoso.com 中创建并链接以下 IPAM GPO（组策略对象）：IPAM1_DHCP、IPAM1_DNS 和 IPAM1_DC_NPS，以允许名为 IPAMUG 的通用组进行访问。此外，该 cmdlet 将 GPO 编辑权限委托给用户 NetworkAdmin1 和 NetworkAdmin2，并使用域范围内的 DNS 访问控制列表（ACL）为名为 IPAMUG 的通用组启用 DNS 读取访问功能。同时，该 cmdlet 还会抑制默认的确认提示信息显示。

### 示例 5：配置组策略对象（GPO）并委派其管理权限
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "child.contoso.com" -GpoPrefixName "IPAM1" -DelegatedGpoGroup "IPAMAdmins" -Force
```

此命令会在域 child.contoso.com 中创建一个名为 IPAMUG 的通用组（如果该组还不存在的话），并将运行 IPAM 服务器的本地计算机的账户添加到该组中。此外，此cmdlet还会在 domain.child.contoso.com 域内创建并链接以下三个 IPAM GPO（IPAM1_DHCP、IPAM1_DNS 和 IPAM1_DC_NPS），以便使名为 IPAMUG 的通用组能够访问这些资源。同时，该cmdlet 将 GPO 编辑权限委托给名为 IPAMAdmins 的组；并通过域范围内的 DNS 访问控制列表（ACL）为名为 IPAMUG 的通用组启用 DNS 读取权限；最后，此 cmdlet 会抑制默认的确认提示信息。

### 示例 6：配置组策略对象（GPO）并输出相关结果
```
PS C:\> Invoke-IpamGpoProvisioning -Domain "Ds2-infra.Contoso.com" -GpoPrefixName "IPAM1" -PassThru -Force
DisplayName : IPAM1_DNS
DomainName : ds2-infra.contoso.com
Owner : DS2-INFRA\Domain Admins
Id : ac9dcf5e-8581-442d-ba12-ae7569985313
GpoStatus : AllSettingsEnabled
Description :
CreationTime : 2/7/2012 1:04:18 AM
ModificationTime : 2/7/2012 1:04:28 AM
UserVersion : AD Version: 1, SysVol Version: 1
ComputerVersion : AD Version: 1, SysVol Version: 1
WmiFilter :

DisplayName : IPAM1_DC_NPS
DomainName : ds2-infra.contoso.com
Owner : DS2-INFRA\Domain Admins
Id : 5aaf16d7-9818-47c4-ade9-3860bc00c292
GpoStatus : AllSettingsEnabled
Description :
CreationTime : 2/7/2012 1:04:19 AM
ModificationTime : 2/7/2012 1:04:28 AM
UserVersion : AD Version: 1, SysVol Version: 1
ComputerVersion : AD Version: 1, SysVol Version: 1
WmiFilter :

DisplayName : IPAM1_DHCP
DomainName : ds2-infra.contoso.com
Owner : DS2-INFRA\Domain Admins
Id : 51fb3dee-0032-4d9a-8b92-84af318dcb51
GpoStatus : AllSettingsEnabled
Description :
CreationTime : 2/7/2012 1:04:20 AM
ModificationTime : 2/7/2012 1:04:28 AM
UserVersion : AD Version: 1, SysVol Version: 1
ComputerVersion : AD Version: 1, SysVol Version: 1
WmiFilter :
```

此命令会在域 child.contoso.com 中创建一个名为 IPAMUG 的通用组（如果该组还不存在的话），并将运行 IPAM 服务器的本地计算机的账户添加到该组中。此外，此 cmdlet 还会在域 Ds2-infra.Contoso.com 中创建并链接以下三个 IPAM GPO（IPAM1_DHCP、IPAM1_DNS 和 IPAM1_DC_NPS），以使名为 IPAMUG 的通用组能够访问相关资源。同时，该 cmdlet 使用域范围内的 DNS 访问控制列表 (ACL) 为名为 IPAMUG 的通用组启用 DNS 读取权限。此外，此 cmdlet 会抑制默认的确认提示信息，并输出在此操作过程中创建的所有 GPO。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DelegatedGpoGroup
指定一个由逗号分隔的域名组列表，这些域名组被授予了对通过此 cmdlet 创建的三个 IPAM GPO（组策略对象）进行编辑的权限。这些组默认具有 `Edit settings, Delete, Modify Security` 的 GPO 编辑权限。对于没有域管理员权限的用户或组，也可以通过 GPMC 或 GPO cmdlets 为现有的 IPAM GPO 启用相应的编辑权限。运行 IPAM 服务器的计算机会利用这些权限，在登录用户的身份上下文中自动修改 GPO 过滤器列表；该用户是从 IPAM 服务器库存视图来修改服务器管理状态的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DelegatedGpoUser
指定一个由逗号分隔的域用户列表，这些用户被授予了对通过此 cmdlet 创建的三个 IPAM GPO 的编辑权限。这些用户被赋予了标准的 GPO 委派权限（包括“编辑设置”、“删除”和“修改安全设置”）。对于没有域管理员权限的用户或组，也可以通过 GPMC 或 GPO cmdlets 为现有的 IPAM GPO 启用相应的委派功能。运行 IPAM 服务器的计算机会利用这种委派机制，在登录用户的权限范围内自动更新 GPO 过滤器列表；该用户正在从 IPAM 服务器的库存视图中修改服务器的管理状态。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Domain
指定用于创建和链接 IPAM 组策略对象（GPO）的域的完全限定域名（FQDN）。每次仅指定一个域名。对于 Active Directory （AD）林中需要由运行 IPAM 服务器的计算机管理的每个域，都需要分别调用此 cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainController
指定用于完成 GPO 操作的域控制器的名称。可以指定该域控制器的完全 Qualified Domain Name (FQDN)，也可以仅指定其主机名。必须提供与所指定域名相匹配的有效域控制器名称。默认情况下，运行 IPAM 服务器的计算机会联系该域的 PDC（Primary Domain Controller）模拟器，除非明确指定了其他参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令执行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GpoPrefixName
指定在创建组策略对象时使用的唯一 GPO 前缀名称。此处指定的 GPO 前缀名称（例如 IPAMGPO_ServerX）必须与在 IPAM 配置向导中选择基于组策略的配置方法时所指定的前缀名称相同。这三个 IPAM GPO 的名称会在该参数值后添加 `_DHCP`、`_DNS` 和 `_DC_NPS` 后缀，例如 IPAMGPO_ServerX_DHCP、IPAMGPO_ServerX_DNS 和 IPAMGPO_ServerX_DC_NPS。这些后缀表示根据运行 IPAM 服务器的计算机所管理的服务器角色类型，它们分别用于传播三种不同的访问设置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamServerFqdn
指定运行 IPAM 服务器的计算机的完全限定域名（FQDN），这些 GPO 将为该服务器启用访问设置。默认情况下，IPAM 会使用执行该命令的语法单元（cmdlet）所在计算机上的 FQDN 来启用访问设置。所指定的计算机账户将被添加到由此 cmdlet 创建的名为 “IPAMUG” 的通用组中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该 cmdlet 被运行时会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Add-IpamCustomField](./Add-IpamCustomField.md)

[Add-IpamCustomValue](./Add-IpamCustomValue.md)

[Export-IpamAddress](./Export-IpamAddress.md)

[Export-IpamRange](./Export-IpamRange.md)

[Get-IpamConfiguration](./Get-IpamConfiguration.md)

[Get-IpamCustomField](./Get-IpamCustomField.md)

[Import-IpamAddress](./Import-IpamAddress.md)

[Import-IpamRange](./Import-IpamRange.md)

[Set-IpamConfiguration](./Set-IpamConfiguration.md)

