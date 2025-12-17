---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/test-addsdomaincontrollerinstallation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ADDSDomainControllerInstallation
---

# 测试 ADDSDomainController 的安装

## 摘要
仅运行安装 Active Directory 中域控制器所需的先决条件（prerequisites）程序。

## 语法

### ADDSDomainController（默认值）

```
Test-ADDSDomainControllerInstallation -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-SiteName <String>]
 [-ADPrepCredential <PSCredential>] [-AllowDomainControllerReinstall]
 [-ApplicationPartitionsToReplicate <String[]>] [-CreateDnsDelegation]
 [-Credential <PSCredential>] [-CriticalReplicationOnly] [-DatabasePath <String>]
 [-DnsDelegationCredential <PSCredential>] [-NoDnsOnNetwork] [-NoGlobalCatalog]
 [-InstallationMediaPath <String>] [-InstallDns] [-LogPath <String>]
 [-MoveInfrastructureOperationMasterRoleIfNecessary] [-NoRebootOnCompletion]
 [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns] [-SystemKey <SecureString>]
 [-SysvolPath <String>] [-Force] [<CommonParameters>]
```

### ADDSDomainControllerReadOnly

```
Test-ADDSDomainControllerInstallation -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] -SiteName <String>
 [-ADPrepCredential <PSCredential>] [-AllowDomainControllerReinstall]
 [-AllowPasswordReplicationAccountName <String[]>]
 [-ApplicationPartitionsToReplicate <String[]>] [-Credential <PSCredential>]
 [-CriticalReplicationOnly] [-DatabasePath <String>]
 [-DelegatedAdministratorAccountName <String>]
 [-DenyPasswordReplicationAccountName <String[]>] [-NoDnsOnNetwork] [-NoGlobalCatalog]
 [-InstallationMediaPath <String>] [-InstallDns] [-LogPath <String>]
 [-MoveInfrastructureOperationMasterRoleIfNecessary] [-ReadOnlyReplica]
 [-NoRebootOnCompletion] [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns]
 [-SystemKey <SecureString>] [-SysvolPath <String>] [-Force] [<CommonParameters>]
```

### ADDSDomainControllerUseExistingAccount

```
Test-ADDSDomainControllerInstallation -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-ADPrepCredential <PSCredential>]
 [-ApplicationPartitionsToReplicate <String[]>] [-Credential <PSCredential>]
 [-CriticalReplicationOnly] [-DatabasePath <String>] [-NoDnsOnNetwork]
 [-InstallationMediaPath <String>] [-LogPath <String>] [-NoRebootOnCompletion]
 [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns] [-SystemKey <SecureString>]
 [-SysvolPath <String>] [-UseExistingAccount] [-Force] [<CommonParameters>]
```

## 描述

`Test-ADDSDomainControllerInstallation` 这个 cmdlet 仅执行那些在您使用 `Install-ADDSDomainController` cmdlet 在 Active Directory 中安装域控制器时才会进行的先决条件检查。它与使用 `Install-ADDSDomainController` cmdlet 的 **WhatIf** 参数有所不同：该 cmdlet 不会总结安装过程中将会发生的变化，而是实际测试在当前环境下这些变化是否可行。

有关 **ADDSDeployment** 模块在使用此 cmdlet 时执行的这些前提条件检查范围的更多信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中的 “ADPrep 和前提条件检查架构” 部分。

## 示例

### 示例 1：测试是否可以安装域控制器

```powershell
$HashArguments = @{
    Credential = (Get-Credential CORP\Administrator)
    DomainName = "corp.contoso.com"
    InstallDns = $true
}
Test-ADDSDomainControllerInstallation @HashArguments
```

此命令会运行一系列前置步骤，以确定是否可以安装域控制器（该域控制器将为 `corp.contoso.com` 域提供 DNS 服务），并且需要使用域管理员的凭据来执行这些操作。此外，该命令还会提示用户输入并确认目录服务恢复模式（Directory Services Restore Mode，简称 DSRM）的密码。

### 示例 2：测试是否可以安装域控制器和 DNS 服务器

```powershell
Test-ADDSDomainControllerInstallation -InstallDns -DomainName "corp.contoso.com"
```

此命令会运行必要的前置步骤，以确定是否可以在 `corp.contoso.com` 域中安装域控制器和 DNS 服务器。同时，该命令还会提示用户输入并确认 DSRM 密码。

### 示例 3：使用管理员凭据测试是否可以安装域控制器

```powershell
$HashArguments = @{
    Credential = (Get-Credential)
    DomainName = (Read-Host "Domain to promote into")
    InstallDns = $true
}
Test-ADDSDomainControllerInstallation @HashArguments
```

该命令会运行一系列前置检查，以确定是否可以同时安装域控制器和DNS服务器。在此过程中，系统会要求用户输入管理员凭据；同时还会验证所选域名是否有效，并要求用户输入并确认DSRM（Domain System Recovery Manager）的密码。

## 参数

### -ADPrepCredential

指定用于运行操作（如果需要的话）的用户名和密码，这些操作是在安装该域之前为准备 Active Directory 而进行的。可以使用 `Get-Credential` cmdlet 来提示用户输入密码。

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

### -AllowDomainControllerReinstall

这表示即使检测到另一个具有相同名称的域控制器账户，该Cmdlet仍会继续安装这个域控制器。默认情况下，如果发现另一个具有相同名称的域控制器，`Install-ADDSDomainController` Cmdlet将不会继续执行安装操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainController, ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowPasswordReplicationAccountName

指定一个包含用户账户、组账户和计算机账户名称的数组，这些账户的密码可以被复制到此 RODC（只读域控制器）中。如果希望该数组为空，请使用空字符串（`""`）。默认情况下，只有“允许的只读域控制器密码复制组”是被允许使用的。

```yaml
Type: System.String[]
Parameter Sets: ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -ApplicationPartitionsToReplicate

指定一组应用程序目录分区，这些分区将由 DCPromo 进行复制。使用以下格式：`"partition1" "partition2" "partitionN"`。若要复制所有应用程序目录分区，请使用 `*`。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -CreateDnsDelegation

表示该 cmdlet 会创建一个 DNS 委派（delegation），该委派引用正在与域控制器一起安装的新 DNS 服务器。此参数仅适用于集成 Active Directory 的 DNS 环境。如果指定了该参数，则会创建相应的 DNS 委派；如果指定 `$False`，则不会创建任何 DNS 委派。默认情况下，该参数的值会根据当前环境自动计算得出。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainController
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于安装域控制器的账户对应的用户名和密码。可以使用 `Get-Credential` cmdlet 来提示用户输入密码。

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

### -CriticalReplicationOnly

该参数表示：在重启之前，此cmdlet仅执行关键数据的复制操作；随后会在AD DS安装过程中继续完成剩余的复制任务。这样就可以跳过那些非关键性的、且可能耗时较长的复制步骤。非关键性数据的复制会在安装完成后以及计算机重新启动之后进行。默认情况下，该cmdlet会同时执行关键数据和非关键数据的复制操作。

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

### -DatabasePath

指定本地计算机固定磁盘上用于存储域数据库的目录的完整路径（该路径不符合通用命名规范（UNC）），例如 `C:\Windows\NTDS`。默认值为 `%SYSTEMROOT%\NTDS`。

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

### -DelegatedAdministratorAccountName

指定作为该域控制器委托管理员的用户或组的名称。

```yaml
Type: System.String
Parameter Sets: ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DenyPasswordReplicationAccountName

指定一个用户账户、组账户和计算机账户的名称数组，这些账户的密码将不会被复制到此 RODC（Replicated Object Directory Controller）。如果您不想拒绝任何用户或计算机的凭据复制，则可以使用空字符串（`""`）。默认情况下，Administrators（管理员）、Server Operators（服务器操作员）、Backup Operators（备份操作员）、Account Operators（账户操作员）以及 Denied RODC Password Replication Group（被拒绝的 RODC 密码复制组）的用户会被禁止访问该功能。Denied RODC Password Replication Group 默认包括 Cert Publishers（证书发布者）、Domain Admins（域管理员）、Enterprise Admins（企业管理员）、Enterprise Domain Controllers（企业域控制器）、Enterprise Read-Only Domain Controllers（企业只读域控制器）、Group Policy Creator Owners（组策略创建者所有者）、krbtgt 账户和 Schema Admins（架构管理员）。

```yaml
Type: System.String[]
Parameter Sets: ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DnsDelegationCredential

用于指定创建 DNS 委托所需的用户名和密码。如果 `-CreateDnsDelegation` 参数的值已被指定或计算结果为 `$false`，则该 cmdlet 会跳过此参数。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: ADDSDomainController
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName

指定安装或添加域控制器所在域的全限定域名（FQDN）。

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

### -Force

强制命令运行，而无需询问用户确认。

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

该参数表示 cmdlet 会在域控制器上安装并配置 DNS 服务器服务。对于域控制器的安装来说，如果未指定此参数，并且当前域名已经托管和存储了该域的 DNS 名称，则该参数的默认值为 `$true$`，此时会安装 DNS 服务器；否则，如果 DNS 域名托管在 Active Directory 之外，则默认值为 `$false$`，此时不会安装 DNS 服务器。

为了测试DNS域名是否托管在Active Directory之外，此cmdlet使用了一种称为“起始授权（SOA）”类型的DNS查询。例如，如果**DomainName**参数的值为`corp.contoso.com`，Active Directory会针对`corp.contoso.com`执行SOA查询，并确认响应中的区域名称确实是`corp.contoso.com`。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainController, ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallationMediaPath

指定用于安装新域控制器的相关安装介质的位置。

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

### -LogPath

指定本地计算机固定磁盘上用于存放域日志文件的目录的完全限定路径（非 UNC 路径），例如 `C:\Windows\Logs`。默认值为 `%SYSTEMROOT%\NTDS`。

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

### -MoveInfrastructureOperationMasterRoleIfNecessary

该参数表示，如果需要的话，此 cmdlet 会将基础设施主控角色（Infrastructure Master Role）转移到你创建的域控制器上。在指定该参数时，不能同时使用 **NoGlobalCatalog** 参数。如果你希望基础设施主控角色保持在其当前的位置，请不要指定此参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainController, ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoDnsOnNetwork

表示网络中无法使用DNS服务。此参数仅在计算机的网络适配器的IP设置未配置用于名称解析的DNS服务器名称时使用。如果该计算机已安装了用于名称解析的DNS服务器，则无需此参数；否则，必须先为网络适配器的IP设置配置DNS服务器的地址。

如果省略此参数（默认值），则表示将使用该服务器计算机上网络适配器的TCP/IP客户端设置来连接DNS服务器。因此，如果您没有指定此参数，请确保先配置TCP/IP客户端设置，为其指定首选的DNS服务器地址。

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

这表示该只读域控制器（RODC）不是全局目录服务器。默认情况下，您正在安装的域控制器是全局目录服务器。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainController, ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoRebootOnCompletion

该参数表示：在执行安装域控制器的操作完成后，此 cmdlet 不会重启计算机。默认情况下，如果省略此参数，则会在安装操作完成时自动重启计算机。微软支持通常建议不要使用此参数（除非用于测试或故障排除），因为一旦配置完成，服务器在重新启动之前将无法正常作为成员服务器或域控制器运行。

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

### -ReadOnlyReplica

表示此cmdlet会将域控制器安装为现有域的RODC（Rental Domain Controller，即租赁域控制器）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerReadOnly
Aliases:

Required: False
Position: Named
Default value: FALSE
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationSourceDC

指定用作复制源的域控制器的名称，以便将数据复制到该域控制器上。

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

当计算机在安全模式（或类似的安全模式，如目录服务恢复模式）下启动时，此参数会提供管理员账户的密码。如果未为该参数指定任何值，cmdlet 会提示您输入并确认一个经过屏蔽处理的密码；如果指定了密码值，则该值必须是一个安全的字符串。

当计算机在安全模式（或类似的安全模式，如目录服务恢复模式）下启动时，系统会要求您提供管理员账户的密码。您提供的密码必须符合域的密码复杂性规则，并且不能为空。如果指定了密码值，该值必须是安全的字符串。

如果未指定此参数，cmdlet 会提示您输入并确认一个屏蔽后的密码。这是交互式运行该 cmdlet 时的推荐用法。此外，如果未向 cmdlet 指定其他参数，系统也会提示您为此参数输入一个屏蔽后的密码，但不会对输入的密码进行任何验证。不建议这样做，因为这样可能会导致配置错误的密码。另一个可用的高级选项是使用 `ConvertTo-SecureString` cmdlet，并将密码字符串作为未屏蔽的 console 输入直接传递给该 cmdlet；然而，在生产环境中，这同样不符合安全最佳实践。

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

指定一个现有站点的名称，您可以将新的域控制器放置在该站点上。默认值取决于安装类型：对于新创建的森林（new forest），默认值为 `Default-First-Site-Name`；对于其他所有类型的安装，默认值是与包含该服务器 IP 地址的子网关联的站点。如果不存在这样的站点，则默认值为复制源域控制器的所在站点。

```yaml
Type: System.String
Parameter Sets: ADDSDomainController
Aliases:

Required: False
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: System.String
Parameter Sets: ADDSDomainControllerReadOnly
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipAutoConfigureDns

表示该cmdlet会跳过DNS客户端设置、转发器和根提示的自动配置步骤。此参数仅在已安装DNS服务器服务的情况下才生效。

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

### -SystemKey

指定用于复制数据的媒体的系统密钥。默认值为“无”。

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

### -SysvolPath

指定本地计算机固定磁盘上一个目录的完全限定路径（非 UNC 路径），该目录将用于存储 Sysvol 数据，例如 `C:\Windows\SYSVOL`。默认值为 `%SYSTEMROOT%\SYSVOL`。

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

### -UseExistingAccount

表示该 cmdlet 将一台服务器附加到现有的 RODC（远程域控制器）账户上。如果指定了相应的权限，Domain Admins 组的成员或被委托的用户就可以运行此 cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ADDSDomainControllerUseExistingAccount
Aliases:

Required: False
Position: Named
Default value: FALSE
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[理解并解决 AD DS 简化管理中的问题](https://go.microsoft.com/fwlink/?LinkID=237244)

[Install-ADDSDomainController](./Install-ADDSDomainController.md)

[测试-添加只读域控制器账户创建功能](./Test-ADDSReadOnlyDomainControllerAccountCreation.md)

[测试 ADDSDomain 安装过程](./Test-ADDSDomainInstallation.md)

[测试-添加森林安装](./Test-ADDSForestInstallation.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
