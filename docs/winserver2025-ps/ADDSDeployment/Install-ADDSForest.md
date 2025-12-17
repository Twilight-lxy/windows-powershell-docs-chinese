---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/install-addsforest?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-ADDSForest
---

# 安装 AD DS 林（Install-ADDSForest）

## 摘要
创建一个新的 Active Directory 林（即一个包含多个域的系统架构）。

## 语法

```
Install-ADDSForest [-SkipPreChecks] -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-CreateDnsDelegation]
 [-DatabasePath <String>] [-DnsDelegationCredential <PSCredential>] [-NoDnsOnNetwork]
 [-DomainMode <DomainMode>] [-DomainNetbiosName <String>] [-ForestMode <ForestMode>]
 [-InstallDns] [-LogPath <String>] [-NoRebootOnCompletion] [-SkipAutoConfigureDns]
 [-SysvolPath <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-ADDSForest` cmdlet 用于安装 Active Directory 林配置。

## 示例

#### 示例 1：安装一个新的森林（森林在这里指的是一个虚拟化的网络环境或计算资源池）

```powershell
Install-ADDSForest -DomainName "corp.contoso.com" -InstallDNS
```

此命令会安装一个名为 `corp.contoso.com` 的新林（forest），系统会提示用户输入并确认目录服务恢复模式（Directory Services Restore Mode，简称 DSRM）的密码，并指定在安装新林的过程中同时需要安装 DNS 服务器。

### 示例 2：安装一个新的林（forest）并设置 DNS 委派（DNS delegation）

```powershell
$HashArguments = @{
    CreateDNSDelegation = $true
    DatabasePath        = "d:\NTDS"
    DomainMode          = Win2008R2
    DomainName          = "corp.contoso.com"
    ForestMode          = Win2008R2
    LogPath             = "e:\Logs"
    SysvolPath          = "d:\SYSVOL"
}
Install-ADDSForest @HashArguments
```

此命令会安装一个名为 `corp.contoso.com` 的新森林（即新的 Active Directory 域），在 `contoso.com` 域中创建 DNS 委派设置，将域的功能级别设置为 Windows Server 2008 R2，并将整个森林的功能级别也设置为 Windows Server 2008。同时，该命令还会在 `D:\` 驱动器上安装 Active Directory 数据库和 SYSVOL 文件系统，在 `E:\` 驱动器上存放日志文件。在 Active Directory 域服务 (AD DS) 安装完成后，服务器会自动重启，并提示用户输入并确认 DSRM 密码。

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

### -CreateDnsDelegation

表示此cmdlet会创建一个DNS委派关系，该关系引用与您一起安装的新的DNS服务器以及域控制器。仅适用于集成到Active Directory中的DNS系统。默认值会根据环境自动计算得出。

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

指定本地计算机固定磁盘上包含域数据库的目录的完全限定路径（该路径不遵循通用命名规范（UNC）），例如 `C:\Databases\NTDS`。默认值为 `%SYSTEMROOT%\NTDS`。

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

指定用于创建 DNS 委托的用户名称和密码。如果 **CreateDnsDelegation** 参数的值已被指定，或者计算结果为 `$false`，则此参数将被忽略。

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

指定在新森林创建过程中第一个域的域功能级别。此参数支持的值可以是有效的整数，也可以是相应的枚举字符串值。例如，要将域模式级别设置为 Windows Server 2008 R2，您可以指定值 `4` 或 `Win2008R2`。

该参数的可接受值为：

- Windows Server 2003:  2 or Win2003
- Windows Server 2008:  3 or Win2008
- Windows Server 2008 R2:  4 or Win2008R2
- Windows Server 2012:  5 or Win2012
- Windows Server 2012 R2:  6 or Win2012R2
- Windows Server 2016: 7 or WinThreshold

The domain functional level cannot be lower than the forest functional level, but it can be higher.
The default is automatically computed and set.

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

### -DomainName

Specifies the fully qualified domain name (FQDN) for the root domain in the forest.

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

### -DomainNetbiosName

Specifies the NetBIOS name for the root domain in the new forest. For NetBIOS names to be valid for
use with this parameter they must be single label names of 15 characters or less.

If this parameter is set with a valid NetBIOS name value, then forest installation continues with
the name specified. If this parameter is not set, then the default is automatically computed from
the value of the **DomainName** parameter.

For example, if this parameter is not specified and a single-label prefix domain name of 15
characters or less is specified within the value of the **DomainName** parameter, then promotion
continues with an automatically generated NetBIOS domain name. For example, the prefix label `corp`
within a full domain name value of `corp.contoso.com` would be a successful name choice.

Note that if the name value given for this parameter is a name of 16 characters or more, then the
forest installation fails.

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

### -Force

Forces the command to run without asking for user confirmation.

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

### -ForestMode

Specifies the forest functional level for the new forest. Supported values for this parameter can
be either a valid integer or a corresponding enumerated string value. For example, to set the
forest mode level to Windows Server 2008 R2, you can specify either a value of `4` or `Win2008R2`.

该参数的可接受值为：

- Windows Server 2003:  2 or Win2003
- Windows Server 2008:  3 or Win2008
- Windows Server 2008 R2:  4 or Win2008R2
- Windows Server 2012:  5 or Win2012
- Windows Server 2012 R2:  `6` or `Win2012R2`
- Windows Server 2016: `7` or `WinThreshold`

The default forest functional level in Windows Server is typically the same as the version you are
running. However, the default forest functional level in Windows Server 2008 R2 when you create a
new forest is Windows Server 2003 or `2`.

```yaml
Type: System.DirectoryServices.ActiveDirectory.ForestMode
Parameter Sets: (All)
Aliases:
Accepted values: Win2008, Win2008R2, Win2012, Win2012R2, WinThreshold, Default

Required: False
Position: Named
Default value: Windows2008R2
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallDns

Indicates that this cmdlet installs and configures the DNS Server service for the new forest.
For forest installation, the default is `$true`.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogPath

Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local computer
where the log file for this operation is written. For instance, `C:\Logs`. The default log file path
if no other path is specified with this parameter is `%SYSTEMROOT%\NTDS`.

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

Indicates that the DNS service is not available on the network. This parameter is used only when the
IP setting of the network adapter for this computer is not configured with the name of a DNS server
for name resolution. It indicates that a DNS server is installed on this computer for name
resolution. Otherwise, the IP settings of the network adapter must first be configured with the
address of a DNS server.

Omitting this parameter indicates that the TCP/IP client settings of the network adapter on this
server computer is used to contact a DNS server. Therefore, if you do not specify this parameter,
ensure that TCP/IP client settings are first configured with a preferred DNS server address.

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

Indicates that the cmdlet does not reboot the computer upon completion of this command. Omitting
this parameter indicates the computer is rebooted upon completion of the command, regardless of
success or failure. As a general rule, Microsoft support recommends that you do not use this
parameter except for testing or troubleshooting purposes because once configuration has completed
the server will not function correctly as either a member server or a DC until it is rebooted.

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

### -SafeModeAdministratorPassword

Supplies the password for the administrator account when the computer is started in Safe Mode or a
variant of Safe Mode, such as Directory Services Restore Mode. You must supply a password that meets
the password complexity rules of the domain and the password cannot be blank. If specified with a
value, the value must be a secure string.

If this parameter is not specified, the cmdlet prompts you to enter and confirm a masked password.
This is the preferred usage when running the cmdlet interactively. If additionally there are no
other arguments specified with the cmdlet, you are prompted to enter a masked password for this
parameter but no confirmation of the password entered is made. This is not recommended as it could
allow a mistyped password to be configured. Another available advanced option is to use the
`ConvertTo-SecureString` cmdlet and specify the password string inline as unmasked console input,
which is also not a recommended security best practice in production deployments.

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipAutoConfigureDns

Indicates that the cmdlet skips automatic configuration of DNS client settings, forwarders, and root
hints. This parameter is in effect only if the DNS Server service is already installed.

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

Indicates that the cmdlet performs only a base set of validations. This behavior is equivalent to
the validations that were performed when using `Dcpromo.exe` in earlier versions of Windows Server
to add a new forest. When this switch parameter is set, it specifies that additional preliminary
checks should be bypassed. For more information on the scope of these additional preliminary checks
that the **ADDSDeployment** module performs by default when using Windows Server 2012, refer to the
table in the section ADPrep and Prerequisite Checking Architecture in
[简化AD DS管理](https://go.microsoft.com/fwlink/?LinkID=237244).

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

Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local computer
where the Sysvol file is written. For example, `C:\Logs\SYSVOL`. The default path if no other path
is specified with this parameter is `%SYSTEMROOT%\SYSVOL`.

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

- By default, the DNS Server service is installed when you create a new forest. It is strongly
  recommended that you install and use the Windows DNS Server to support the needs for DNS name
  resolution in your Active Directory deployment. You do not need to specifically include the
  `-InstallDNS` to install it.

- If you are using Active Directory-integrated DNS, the IP address for the preferred DNS server for
  the first domain controller in the forest is automatically set to the loopback address of
  `127.0.0.1`. This helps assure that the IP address of the first domain controller is resolved in
  DNS even if the address is changed.

## 相关链接

[简化AD DS管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[Install-ADDSDomain](./Install-ADDSDomain.md)

[测试-ADDS森林安装](./Test-ADDSForestInstallation.md)

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)
