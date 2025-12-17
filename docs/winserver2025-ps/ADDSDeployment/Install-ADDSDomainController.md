---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/install-addsdomaincontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-ADDSDomainController
---

# 安装 ADDSDomainController

## 摘要
在 Active Directory 域中安装一个新的域控制器。

## 语法

### ADDSDomainController（默认值）

```
Install-ADDSDomainController [-SkipPreChecks] -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-SiteName <String>]
 [-ADPrepCredential <PSCredential>] [-AllowDomainControllerReinstall]
 [-ApplicationPartitionsToReplicate <String[]>] [-CreateDnsDelegation] [-Credential <PSCredential>]
 [-CriticalReplicationOnly] [-DatabasePath <String>] [-DnsDelegationCredential <PSCredential>]
 [-NoDnsOnNetwork] [-NoGlobalCatalog] [-InstallationMediaPath <String>] [-InstallDns]
 [-LogPath <String>] [-MoveInfrastructureOperationMasterRoleIfNecessary] [-NoRebootOnCompletion]
 [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns] [-SystemKey <SecureString>]
 [-SysvolPath <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADDSDomainControllerReadOnly

```
Install-ADDSDomainController [-SkipPreChecks] -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] -SiteName <String>
 [-ADPrepCredential <PSCredential>] [-AllowDomainControllerReinstall]
 [-AllowPasswordReplicationAccountName <String[]>] [-ApplicationPartitionsToReplicate <String[]>]
 [-Credential <PSCredential>] [-CriticalReplicationOnly] [-DatabasePath <String>]
 [-DelegatedAdministratorAccountName <String>] [-DenyPasswordReplicationAccountName <String[]>]
 [-NoDnsOnNetwork] [-NoGlobalCatalog] [-InstallationMediaPath <String>] [-InstallDns]
 [-LogPath <String>] [-MoveInfrastructureOperationMasterRoleIfNecessary] [-ReadOnlyReplica]
 [-NoRebootOnCompletion] [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns]
 [-SystemKey <SecureString>] [-SysvolPath <String>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ADDSDomainControllerUseExistingAccount

```
Install-ADDSDomainController [-SkipPreChecks] -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-ADPrepCredential <PSCredential>]
 [-ApplicationPartitionsToReplicate <String[]>] [-Credential <PSCredential>]
 [-CriticalReplicationOnly] [-DatabasePath <String>] [-NoDnsOnNetwork]
 [-InstallationMediaPath <String>] [-LogPath <String>] [-NoRebootOnCompletion]
 [-ReplicationSourceDC <String>] [-SkipAutoConfigureDns] [-SystemKey <SecureString>]
 [-SysvolPath <String>] [-UseExistingAccount] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-ADDSDomainController` cmdlet 用于在 Active Directory 中安装域控制器。

## 示例

### 示例 1：安装域控制器和 DNS 服务器

```powershell
Install-ADDSDomainController -InstallDns -DomainName "corp.contoso.com"
```

此命令使用 `CORP\Administrator` 凭据在 `corp.contoso.com` 域中安装一个域控制器和 DNS 服务器，并提示用户提供并确认目录服务恢复模式（DSRM）的密码。

### 示例 2：使用管理员凭据安装域控制器和 DNS 服务器

```powershell
$HashArguments = @{
    Credential = (Get-Credential "CORP\Administrator")
    DomainName = "corp.contoso.com"
    InstallDns = $true
}
Install-ADDSDomainController @HashArguments
```

该命令使用管理员凭据在 `corp.contoso.com` 域中安装一个域控制器和 DNS 服务器，并提示用户提供并确认 DSRM 密码。

### 示例 3：安装一个域控制器和 DNS 服务器，并使用域名提升（domain promotion）功能

```powershell
$HashArguments = @{
    Credential = (Get-Credential)
    DomainName = (Read-Host "Domain to promote into")
    InstallDns = $true
}
Install-ADDSDomainController @HashArguments
```

安装域控制器和DNS服务器，并会提示用户输入凭据、用于安装及提升域控制器权限的域名，以及输入并确认DSRM密码。

## 参数

### -ADPrepCredential

指定用于运行 Adprep 实用程序的用户名和密码（如果需要的话）。该实用程序用于在安装此域控制器之前准备相应的目录。可以使用 `Get-Credential` cmdlet 来提示用户输入密码。

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

这表示即使检测到另一个具有相同名称的域控制器账户，该cmdlet仍会继续安装这个域控制器。默认情况下，如果找到另一个具有相同名称的域控制器，`Install-ADDSDomainController` cmdlet不会继续进行安装。

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

指定一个用户账户、组账户和计算机账户的名称数组，这些账户的密码可以被复制到这个读写受限域控制器（RODC）中。如果希望该数组为空，请使用空字符串（`""`）。默认情况下，只有允许访问的只读域控制器（RODC）密码复制组被允许使用此功能。

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

指定一组应用程序目录分区，这些分区将被 DCPromo 复制。使用以下格式：`"partition1" "partition2" "partitionN"`。如果需要复制所有应用程序目录分区，则使用 `*`。

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

表示该 cmdlet 会创建一个 DNS 委派（delegation），该委派指向由该 cmdlet 与域控制器一同安装的新 DNS 服务器。此参数仅适用于集成 Active Directory 的 DNS 环境。如果指定了该参数，则会创建相应的 DNS 委派；如果指定 `$False`，则不会创建任何 DNS 委派。默认情况下，该参数的值会根据当前环境自动计算得出。

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

指定用于安装域控制器的账户的用户名和密码。可以使用 `Get-Credential` 命令来提示用户输入密码。

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

该参数表示：在重启之前，此cmdlet仅执行关键数据的复制操作；随后在AD DS安装过程中继续完成剩余的复制任务。这样一来，系统可以跳过那些非关键且可能耗时较长的复制步骤。非关键数据的复制会在安装完成后、计算机重新启动时再进行。默认情况下，该cmdlet会同时执行关键数据和非关键数据的复制操作。

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

指定本地计算机固定磁盘上某个目录的完全限定路径（该路径不遵循通用命名约定（UNC）），该目录将用于存储域数据库。例如，路径可以是 `C:\Windows\NTDS`。默认值为 `%SYSTEMROOT%\NTDS`。

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

指定不应将其密码复制到此 RODC（Replicated Operations Domain Controller）的用户账户、组账户和计算机账户的名称。如果您不希望拒绝任何用户或计算机的凭据复制，请使用空字符串（`""`）。默认情况下，管理员（Administrators）、服务器操作员（Server Operators）、备份操作员（Backup Operators）、账户操作员（Account Operators）以及“被拒绝的 RODC 密码复制组”（Denied RODC Password Replication Group）的用户会被禁止访问该功能。该“被拒绝的 RODC 密码复制组”包括证书发布者（Cert Publishers）、域管理员（Domain Admins）、企业管理员（Enterprise Admins）、企业只读域控制器（Enterprise Read-Only Domain Controllers）、组策略创建者所有者（Group Policy Creator Owners）、krbtgt 账户以及架构管理员（Schema Admins）。

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

指定用于创建DNS委派的用户名和密码。如果**CreateDnsDelegation**参数的值已经被指定，或者计算结果为`$false`，则此参数将被忽略。

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

指定用于安装或添加域控制器的域的完全限定域名（FQDN）。

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

强制命令运行，而不需要用户确认。

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

该参数表示 cmdlet 会在域控制器上安装并配置 DNS 服务器服务。对于域控制器的安装，如果未指定此参数且当前域已经托管并存储了该域的 DNS 名称，则该参数的默认值为 `$true$`，此时会安装 DNS 服务器；否则，如果 DNS 域名称托管在 Active Directory 之外，则该参数的默认值为 `$false$`，此时不会安装 DNS 服务器。

为了检测DNS域名是否托管在Active Directory之外，此cmdlet使用了一种称为“起始授权（SOA）”类型的DNS查询。例如，如果**DomainName**的值为`corp.contoso.com`，Active Directory会针对`corp.contoso.com`执行SOA查询，并确保响应中的区域名称确实是`corp.contoso.com`。

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

用于指示安装新域控制器时所使用的安装介质的位置。

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

指定本地计算机固定磁盘上用于存放域日志文件的目录的完整路径（非 UNC 路径），例如 `C:\Windows\Logs`。默认值为 `%SYSTEMROOT%\NTDS`。

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

该参数表示此 cmdlet 会将基础设施主控角色（Infrastructure Master Role）转移到正在安装的域控制器上。为了成功完成转移操作，还必须同时使用 **NoGlobalCatalog** 参数。如果您希望基础设施主控角色保持在其当前的位置，请不要指定该参数。

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

表示网络中无法使用DNS服务。此参数仅在计算机的网络适配器的IP设置未配置DNS服务器名称以进行名称解析时使用。如果已在该计算机上安装了DNS服务器以进行名称解析，则无需再使用此参数；否则，必须先为网络适配器的IP设置配置DNS服务器的地址。

如果省略此参数（即使用默认值），则表示将使用该服务器计算机上的网络适配器的TCP/IP客户端设置来连接DNS服务器。因此，如果您没有指定此参数，请确保首先配置TCP/IP客户端设置，为其指定首选的DNS服务器地址。

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

这表示该RODC（Remote Domain Controller）将不会作为全局目录服务器使用。默认情况下，您正在安装的域控制器会充当全局目录服务器的角色。

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

该参数表示：在安装域控制器的操作完成后，此 cmdlet 不会重启计算机。默认情况下，如果省略了这个参数，计算机将在安装操作完成时自动重启。一般来说，微软支持不建议使用此参数（除非用于测试或故障排除），因为配置完成后，服务器在重新启动之前将无法正常作为成员服务器或域控制器运行。

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

表示该cmdlet会将域控制器安装为现有域中的RODC（读-only Domain Controller，只读域控制器）。

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

指定要用作复制源的域控制器的名称，以便将数据复制到该域控制器上。

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

当计算机在安全模式（或类似安全模式的目录服务恢复模式）下启动时，该参数用于提供管理员账户的密码。如果未为该参数指定任何值，cmdlet 会提示您输入并确认一个经过加密处理的密码；如果指定了某个值，则该值必须是一个安全的字符串。

当计算机在安全模式（Safe Mode）或类似的安全模式模式（如目录服务恢复模式 Directory Services Restore Mode）下启动时，需要提供管理员账户的密码。所提供的密码必须符合域的密码复杂性要求，并且不能为空。如果指定了密码值，该值必须是一个安全的字符串。

如果未指定此参数，cmdlet 会提示您输入并确认一个经过加密处理的密码。这是交互式运行该 cmdlet 时的推荐用法。此外，如果未向 cmdlet 指定其他任何参数，系统也会提示您为该参数输入一个加密后的密码，但不会对输入的密码进行再次确认。这种做法并不推荐，因为可能会导致错误的密码被配置进去。另一种高级选项是使用 `ConvertTo-SecureString` cmdlet，并将密码字符串作为未加密的文本直接在控制台中输入；不过，在实际生产环境中，这同样不属于最佳的安全实践。

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

指定一个现有站点的名称，您可以将新的域控制器放置在该站点上。默认值取决于安装类型：对于一个新的森林（domain forest），默认值为 `Default-First-Site-Name`；对于所有其他类型的安装，默认值是与包含该服务器 IP 地址的子网相关联的站点。如果不存在这样的站点，则默认值为复制源域控制器的所在站点。

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

表示该cmdlet会跳过DNS客户端设置、转发器和根提示的自动配置过程。此参数仅在已安装DNS服务器服务的情况下才生效。

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

该参数表示该 cmdlet 仅执行一组基本的验证操作。这种行为等同于在早期版本的 Windows Server 中使用 `Dcpromo.exe` 添加新的域控制器时所执行的验证过程。当设置此参数时，意味着应跳过额外的初步检查步骤。有关 **ADDSDeployment** 模块在使用 Windows Server 2016 时默认执行的其他初步检查的具体内容，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中“ADPrep 和前提条件检查架构”部分中的相关表格。

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

指定本地计算机固定磁盘上包含 Sysvol 数据的目录的完整路径（非 UNC 路径），例如 `C:\Windows\SYSVOL`。默认值为 `%SYSTEMROOT%\SYSVOL`。

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

表示该 cmdlet 将一台服务器附加到现有的 RODC（Windows Active Directory 域控制器）账户上。如果指定了相应的权限，Domain Admins 组的成员或被委托的用户就可以运行此 cmdlet。

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

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.DirectoryServices.Deployment_types.Result

## 备注

- By default, this cmdlet always prompts for confirmation. To bypass confirmation, you need to
  include the **Confirm** parameter and specify a value of `$false`. For example,
  `-Confirm:$false`.
- By default, this cmdlet is always run when executed. To see what will happen if the cmdlet runs
  without executing or committing installation changes, first run the cmdlet using the **WhatIf**
  parameter to show what would happen.

## 相关链接

[简化AD DS管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[添加 AD DS 只读域控制器账户](./Add-ADDSReadOnlyDomainControllerAccount.md)

[Install-ADDSDomain](./Install-ADDSDomain.md)

[安装 AD DS 林](./Install-ADDSForest.md)

[获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
