---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/test-addsforestinstallation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ADDSForestInstallation
---

# 测试 AD DS 林安装过程

## 摘要
运行安装Active Directory新林所需的先决条件程序。

## 语法

```
Test-ADDSForestInstallation -DomainName <String>
 [-SafeModeAdministratorPassword <SecureString>] [-CreateDnsDelegation]
 [-DatabasePath <String>] [-DnsDelegationCredential <PSCredential>] [-NoDnsOnNetwork]
 [-DomainMode <DomainMode>] [-DomainNetbiosName <String>] [-ForestMode <ForestMode>]
 [-InstallDns] [-LogPath <String>] [-NoRebootOnCompletion] [-SkipAutoConfigureDns]
 [-SysvolPath <String>] [-Force] [<CommonParameters>]
```

## 描述

`Test-ADDSForestInstallation` 这个 cmdlet 会执行那些在您使用 `Install-ADDSForest` cmdlet 来安装 Active Directory 新林时需要进行的先决条件检查。它与使用 `Install-ADDSForest` cmdlet 的 **WhatIf** 参数有所不同：该 cmdlet 不是总结安装过程中将会发生的变化，而是实际测试在当前环境下这些变化是否可行。

有关 **ADDSDeployment** 模块在使用此 cmdlet 时执行的这些前提条件检查范围的更多信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中的 “ADPrep 和前提条件检查架构” 部分。

## 示例

### 示例 1：测试森林的安装过程，以确认是否可行

```powershell
Test-ADDSForestInstallation -DomainName "corp.contoso.com" -NoRebootOnCompletion
```

此命令会运行安装名为 `corp.contoso.com` 的新林所需的先决条件，并指定在新林创建后不要重启系统。系统会提示用户提供并确认目录服务恢复模式（Directory Services Restore Mode，简称 DSRM）的密码。

### 示例 2：测试森林的安装过程，以确认是否可行

```powershell
$HashArguments = @{
    CreateDNSDelegation = $true
    DatabasePath        = "D:\NTDS"
    DomainMode          = Win2008
    DomainName          = "corp.contoso.com"
    ForestMode          = Win2008R2
    LogPath             = "E:\Logs"
    SysvolPath          = "D:\SYSVOL"
}
Test-ADDSForestInstallation @HashArguments
```

此命令用于运行安装新林系统所需的预备步骤。这些步骤包括在`contoso.com`域中创建DNS委派、将域的功能级别设置为Windows Server 2008 R2，以及将整个林系统的功能级别也设置为Windows Server 2008 R2。此外，该命令还会在`D:`驱动器上安装Active Directory数据库和SYSVOL文件，在`E:`驱动器上存放日志文件，并在AD DS安装完成后自动重启服务器。系统会提示用户输入并确认DSRM（Domain Services Recovery Manager）的密码。

## 参数

### -CreateDnsDelegation

表示该cmdlet创建了一个DNS委托关系，该委托关系引用了与您一起安装的新的DNS服务器以及域控制器。此选项仅适用于与Active Directory集成的DNS系统。默认值会根据环境自动计算得出。

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

指定本地计算机固定磁盘上包含域数据库的目录的完全限定路径（该路径不符合通用命名规范（UNC）），例如 `C:\Windows\NTDS`。默认值为 `%SYSTEMROOT%\NTDS`。

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

指定用于创建 DNS 委托的用户名称和密码（账户凭据）。如果 `CreateDnsDelegation` 参数的值已被指定或计算结果为 `$false`，则该 cmdlet 将忽略此参数。

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

指定在新森林创建过程中第一个域的域功能级别。该参数支持的值可以是有效的整数，也可以是相应的枚举字符串值。例如，要将域模式级别设置为 Windows Server 2008 R2，可以指定数值 `4` 或字符串 `Win2008R2`。

此参数的可接受值包括：

- Windows Server 2003:  2 or Win2003
- Windows Server 2008:  3 or Win2008
- Windows Server 2008 R2:  4 or Win2008R2
- Windows Server 2012:  5 or Win2012
- Windows Server 2012 R2:  6 or Win2012R2

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

For instance, if this parameter is not specified and a single-label prefix domain name of 15
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

Specifies the forest functional level for the new forest. Supported values for this parameter can be
either a valid integer or a corresponding enumerated string value. For example, to set the forest
mode level to Windows Server 2008 R2, you can specify either a value of `4` or `Win2008R2`.

此参数的可接受值包括：

- Windows Server 2003:  2 or Win2003
- Windows Server 2008:  3 or Win2008
- Windows Server 2008 R2:  4 or Win2008R2
- Windows Server 2012:  `5` or `Win2012`
- Windows Server 2012 R2:  `6` or `Win2012R2`

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

Indicates that the cmdlet installs and configures the DNS Server service for the new forest. For
forest installation, the default is `$true`.

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
server computer is used to contact a DNS server. Therefore, if you are not specifying this
parameter, ensure that TCP/IP client settings are first configured with a preferred DNS server
address.

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

Indicates that the cmdlet does not reboot the computer upon completion of the command.

Omitting this parameter indicates the computer is rebooted upon completion of the command,
regardless of success or failure. As a general rule, Microsoft support recommends that you not use
this parameter except for testing or troubleshooting purposes because once configuration has
completed the server will not function correctly as either a member server or a DC until it is
rebooted.

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

Specifies the password for the administrator account when the computer is started in Safe Mode or a
variant of Safe Mode, such as Directory Services Restore Mode. You must supply a password that meets
the password complexity rules of the domain and the password cannot be blank. If specified with a
value, the value must be a secure string.

If this parameter is not specified, the cmdlet prompts you to enter and confirm a masked password.
This is the preferred usage when running the cmdlet interactively. If there are no other arguments
specified with the cmdlet, you are prompted to enter a masked password for this parameter but no
confirmation of the password entered is made. This is not recommended as it could allow a mistyped
password to be configured. Another available advanced option is to use the
`ConvertTo-SecureString` cmdlet and specify the password string inline as unmasked console input,
which is also not a recommended security best practice in production deployments.

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[简化AD DS管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[Install-ADDSForest](./Install-ADDSForest.md)

[测试-ADDSDomainInstallation](./Test-ADDSDomainInstallation.md)

[测试-ADDSDomainController安装](./Test-ADDSDomainControllerInstallation.md)

[安装 ADDSDomainController](./Install-ADDSDomainController.md)

[将字符串转换为安全字符串](https://go.microsoft.com/fwlink/p/?LinkId=113291)
