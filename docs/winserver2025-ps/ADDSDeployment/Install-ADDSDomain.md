---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/install-addsdomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-ADDSDomain
---

# 安装并添加域（ADDSDomain）

## 摘要

在现有的 Active Directory 林中创建一个新的域。

## 语法

```
Install-ADDSDomain [-SkipPreChecks] -NewDomainName <String> -ParentDomainName <String>
[-SafeModeAdministratorPassword <SecureString>] [-ADPrepCredential <PSCredential>]
[-AllowDomainReinstall] [-CreateDnsDelegation] [-Credential <PSCredential>]
[-DatabasePath <String>] [-DnsDelegationCredential <PSCredential>] [-NoDnsOnNetwork]
[-DomainMode <DomainMode>] [-DomainType <DomainType>] [-NoGlobalCatalog] [-InstallDns]
[-LogPath <String>] [-NewDomainNetbiosName <String>] [-NoRebootOnCompletion]
[-ReplicationSourceDC <String>] [-SiteName <String>] [-SkipAutoConfigureDns]
[-SysvolPath <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-ADDSDomain` cmdlet 用于安装 Active Directory 域配置。

## 示例

#### 示例 1：安装一个新的子域名

```powershell
$params = @{
    Credential = (Get-Credential CORP\EnterpriseAdmin1)
    NewDomainName = "child"
    ParentDomainName = "corp.contoso.com"
    InstallDNS = $true
    CreateDNSDelegation = $true
    DomainMode = "Win2003"
    ReplicationSourceDC = "DC1.corp.contoso.com"
    SiteName = "Houston"
    DatabasePath = "D:\NTDS"
    SYSVOLPath = "D:\SYSVOL"
    LogPath = "E:\Logs"
    NoRebootOnCompletion = $true
}
Install-ADDSDomain @HashArguments
```

此命令使用 `CORP\EnterpriseAdmin1` 的凭据来安装一个名为 `child.corp.contoso.com` 的新子域。该命令还会安装一台 DNS 服务器，在 `corp.contoso.com` 域中创建 DNS 委托关系，将域的功能级别设置为 Windows Server 2003，使域控制器成为位于 “Houston” 站点中的全局目录服务器，并使用 `DC1.corp.contoso.com` 作为复制源域控制器。此外，该命令还会在 `D:\` 驱动器上安装 Active Directory 数据库和 SYSVOL；同时禁止服务器在域安装完成后自动重启，并要求用户提供并确认 “目录服务恢复模式”（DSRM）的密码，以完成并在 Active Directory 中提交域的安装过程。

## 参数

### -ADPrepCredential

指定用于运行操作以准备 Active Directory 的用户名和密码，这些操作将在该域安装之前执行。可以使用 `Get-Credential` cmdlet 来提示用户输入密码。

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

### -AllowDomainReinstall

表示该 cmdlet 会重新创建一个已存在的域。

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

### -CreateDnsDelegation

表示该 cmdlet 会创建一个 DNS 委托（DNS delegation），该委托引用与您安装的域控制器一起部署的新 DNS 服务器。此选项仅适用于集成到 Active Directory 中的 DNS 环境。默认值会根据环境自动计算得出。

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

### -Credential

指定用于安装域控制器的帐户的用户名和密码。可以使用 `Get-Credential` cmdlet 来提示用户输入密码。

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

### -DatabasePath

指定本地计算机固定磁盘上一个目录的完全限定路径（该路径不符合通用命名规范（UNC）），该目录包含域数据库，例如 `C:\Windows\NTDS`。默认值为 `%SYSTEMROOT%\NTDS`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DnsDelegationCredential

指定用于创建 DNS 委托的用户名称和密码（账户凭据）。如果 **CreateDnsDelegation** 参数的值已被指定，或者计算结果为 `$false`，则此参数将被忽略。

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

### -DomainMode

指定在新森林创建过程中第一个域的域功能级别。此参数支持的取值可以是有效的整数，也可以是相应的枚举字符串值。例如，要将域模式级别设置为 Windows Server 2008 R2，可以指定数值 `4` 或字符串 `Win2008R2`。

该参数的可接受值为：

- Windows Server 2003:  2 or Win2003
- Windows Server 2008:  3 or Win2008
- Windows Server 2008 R2:  4 or Win2008R2
- Windows Server 2012:  5 or Win2012
- Windows Server 2012 R2:  6 or Win2012R2
- Windows Server 2016: 7 or Windows2016Domain

域的功能级别不能低于森林的功能级别，但可以高于森林的功能级别。默认值是自动计算并设置的。

```yaml
Type: System.DirectoryServices.ActiveDirectory.DomainMode
Parameter Sets: (All)
Aliases:
Accepted values: Win2008, Win2008R2, Win2012, Win2012R2, WinThreshold, Default

Required: False
Position: Named
Default value: Windows2008R2
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainType

指定此 cmdlet 创建的域类型。您可以在现有的林中创建一个新的域树（支持的值为 `TreeDomain` 或 `Tree`），或者创建一个现有域的子域（支持的值为 `ChildDomain` 或 `Child`）。默认值为 `ChildDomain`。

```yaml
Type: DomainType
Parameter Sets: (All)
Aliases:
Accepted values: ChildDomain, TreeDomain

Required: False
Position: Named
Default value: ChildDomain
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令执行，而无需请求用户确认。

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

### -InstallDns

表示该cmdlet会为指定的域或域树安装并配置DNS服务器服务。对于域的安装来说，如果未指定此参数，并且父域（或在域树的情况下，是森林根域）已经负责存储该域的DNS名称，则该参数的默认值为 `$true`，此时会安装DNS服务器。否则，如果DNS域名托管在Active Directory之外，则该参数的默认值为 `$false$》，此时不会安装DNS服务器。

为了测试DNS域名是否托管在Active Directory之外，此Cmdlet使用了“权威起始（SOA）”类型的DNS查询。例如，如果**NewDomainName**参数的值为`corp.contoso.com`，那么Active Directory会针对`corp.contoso.com`执行一个SOA查询，并确认响应中的区域名称确实是`corp.contoso.com`。

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

### -LogPath

指定本地计算机固定磁盘上包含域日志文件的目录的完全限定路径（非 UNC 路径），例如 `C:\Windows\Logs`。默认值为 `%SYSTEMROOT%\NTDS`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewDomainName

指定此 cmdlet 将安装的新域名。如果将 **DomainType** 参数的值设置为 `TreeDomain`，则可以使用该参数来指定新域树的完全限定域名（FQDN）。如果将 **DomainType** 参数的值设置为 `ChildDomain`，则可以使用该参数来指定子域的单一标签域名。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewDomainNetbiosName

指定新域的NetBIOS名称。要使NetBIOS名称能够与此参数一起使用并保持有效，这些名称必须是长度不超过15个字符的单标签名称。

如果此参数被设置为一个有效的NetBIOS名称值，那么升级过程将继续使用该指定的名称进行。如果未设置此参数，则会自动根据**NewDomainName**参数的值来计算默认名称。

例如，如果未指定此参数，并且在 **NewDomainName** 参数的值中指定了一个长度为 15 个字符或更少的单标签前缀域名，那么升级过程将继续使用自动生成的 NetBIOS 域名进行。例如，在完整的域名 `corp.contoso.com` 中，前缀标签 `corp` 就是一个合适的域名选择。

请注意，如果为该参数指定的名称长度达到或超过16个字符，那么域名安装将会失败。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoDnsOnNetwork

表示网络中无法使用DNS服务。此参数仅在计算机的网卡IP设置未配置DNS服务器名称以进行名称解析时使用。如果计算机上已安装了DNS服务器用于名称解析，则无需再设置该参数；否则，必须先为网卡的IP设置配置DNS服务器的地址。

如果省略此参数（即使用默认值），则表示将使用该服务器计算机上网络适配器的TCP/IP客户端设置来连接DNS服务器。因此，如果您没有指定此参数，请确保先配置TCP/IP客户端的优先DNS服务器地址。

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

### -NoGlobalCatalog

指定该只读域控制器（RODC）不会充当全局目录服务器。默认情况下，您要安装的域控制器会作为全局目录服务器运行。

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

### -NoRebootOnCompletion

表示该cmdlet在完成操作后不会重新启动计算机。默认情况下，如果使用此cmdlet且省略了该参数，则系统会在完成后自动重启。一般来说，微软支持建议不要使用这个参数（除非是为了测试或排查故障），因为配置完成后，服务器在重新启动之前将无法正常作为成员服务器或域控制器（DC）运行。

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

### -ParentDomainName

指定现有父域的完全限定域名（FQDN）。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationSourceDC

指定用作复制到该域的源的域控制器的完全限定域名（FQDN）。此参数的默认值会从环境中自动计算得出。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -SafeModeAdministratorPassword

当计算机在安全模式（Safe Mode）或其变体（如目录服务恢复模式，Directory Services Restore Mode）下启动时，此参数用于指定管理员账户的密码。您必须提供一个符合域密码复杂度规则的密码，并且该密码不能为空。如果指定了密码值，那么该值必须是一个安全的字符串。

如果未指定此参数，该cmdlet会提示您输入并确认一个经过掩码处理的密码。这是交互式运行该cmdlet时的推荐用法。如果您没有为该cmdlet指定其他参数，则系统会提示您输入一个经过掩码处理的密码，但不会对所输入的密码进行任何确认。这种做法并不推荐，因为这可能会导致错误的密码被配置到系统中。另一个高级选项是使用`ConvertTo-SecureString` cmdlet，并将密码字符串以未屏蔽的形式直接作为控制台输入来指定；然而，在生产环境中，这也并非最佳的安全实践。

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

### -SiteName

指定一个现有站点的名称，您可以将新的域控制器放置在该站点上。默认值是与包含该服务器 IP 地址的子网关联的站点。如果不存在这样的站点，则默认值为复制源域控制器的所在站点。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipAutoConfigureDns

表示该cmdlet会跳过DNS客户端设置、转发器和根提示的自动配置过程。此参数仅在已安装DNS服务器服务的情况下才有效。

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

### -SkipPreChecks

该参数表示该 cmdlet 仅执行最基本的一组验证操作。这种行为等同于在早期版本的 Windows Server 中使用 `Dcpromo.exe` 添加新域时所执行的验证过程。当设置此参数时，表示应跳过额外的初步检查。有关 **ADDSDeployment** 模块在使用 Windows Server 2012 时默认执行的其他初步检查的详细信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中“ADPrep 和前提条件检查架构”部分中的表格。

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

### -SysvolPath

指定本地计算机固定磁盘上某个目录的完全限定路径（非 UNC 路径），例如 `C:\Windows\SYSVOL`。默认值为 `%SYSTEMROOT%\SYSVOL`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

- When a new domain tree is created in an existing forest, a two-way, transitive tree root trust is
  established by default.

## 相关链接

[简化 AD DS 管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[安装-ADDSDomainController](./Install-ADDSDomainController.md)

[安装 AD DS 林](./Install-ADDSForest.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
