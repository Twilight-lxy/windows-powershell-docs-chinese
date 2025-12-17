---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/test-addsreadonlydomaincontrolleraccountcreation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ADDSReadOnlyDomainControllerAccountCreation
---

# 测试 AD DS 是否支持只读域控制器的账户创建功能

## 摘要
运行用于添加 RODC 账户的先决条件所需的相关命令/脚本等。

## 语法

```
Test-ADDSReadOnlyDomainControllerAccountCreation -DomainControllerAccountName <String>
 -DomainName <String> -SiteName <String> [-AllowPasswordReplicationAccountName <String[]>]
 [-Credential <PSCredential>] [-DelegatedAdministratorAccountName <String>]
 [-DenyPasswordReplicationAccountName <String[]>] [-NoGlobalCatalog] [-InstallDns]
 [-ReplicationSourceDC <String>] [-Force] [<CommonParameters>]
```

## 描述

`Test-ADDSReadOnlyDomainControllerAccountCreation` 这个 cmdlet 会执行一些前提检查，这些检查类似于在使用 `Add-ADDSReadOnlyDomainControllerAccount` cmdlet 添加只读域控制器（RODC）账户时需要进行的检查。它与使用 `Add-ADDSReadOnlyDomainControllerAccount` cmdlet 时的 **WhatIf** 参数有所不同：该 cmdlet 并不会仅仅总结账户创建过程中将会发生的变化，而是实际测试在当前环境下这些变化是否可行。

## 示例

### 示例 1：测试添加一个 RODC 账户以确认其是否可行

```powershell
$HashArguments = @{
    DomainControllerAccountName = RODC1
    DomainName                  = "corp.contoso.com"
    SiteName                    = "NorthAmerica"
}
Test-ADDSReadOnlyDomainControllerAccountCreation @HashArguments
```

此命令会运行将 RODC 账户添加到 `corp.contoso.com` 域所需的预备步骤。该账户会将北美站点作为复制源域控制器的源站点。

## 参数

### -AllowPasswordReplicationAccountName

指定可以将其密码复制到此RODC的用户账户、组账户和计算机账户的名称。如果希望该值保持为空，请使用`None`。默认情况下，仅允许“允许的RODC密码复制组”（Allowed RODC Password Replication Group）进行密码复制操作，且该组最初是空状态创建的。

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

### -DelegatedAdministratorAccountName

指定安装和管理 RODC 的用户或组的名称。

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

### -DenyPasswordReplicationAccountName

指定那些用户名、组名以及计算机账户的名称，这些账户的密码将不会被复制到该 RODC（Replicated Operating Domain Controller）中。如果您不想拒绝任何用户或计算机的凭证复制，请使用 `None`。默认情况下，Administrators（管理员）、Server Operators（服务器操作员）、Backup Operators（备份操作员）、Account Operators（帐户操作员）以及 “Denied RODC Password Replication Group” 组的成员被禁止访问该功能。此外，“ Denied RODC Password Replication Group” 还包括 Cert Publishers（证书发布者）、Domain Admins（域管理员）、Enterprise Admins（企业管理员）、Enterprise Domain Controllers（企业域控制器）、Enterprise Read-Only Domain Controllers（企业只读域控制器）、Group Policy Creator Owners（组策略创建者所有者）、krbtgt 账户以及 Schema Admins（架构管理员）。

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

### -DomainControllerAccountName

指定此cmdlet创建的RODC账户的名称。

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

### -DomainName

指定用于操作的用户名称的域名。此参数是必需的。您应该指明计划安装域控制器或创建RODC账户的森林（domain forest）。

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

### -InstallDns

表示该cmdlet用于安装DNS服务器服务。默认设置会根据环境自动计算得出。

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

### -NoGlobalCatalog

表示该 RODC（Root Domain Controller）不是全局目录服务器。

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

### -ReplicationSourceDC

指定用于在 Active Directory 中创建 RODC 账户的全可写域控制器的名称。

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

### -SiteName

指定一个现有站点名称，您可以在该站点上放置新的域控制器。默认值取决于安装类型：对于新创建的森林（domain tree），默认值为 `Default-First-Site-Name`；对于其他所有类型的安装，默认值是与包含该服务器 IP 地址的子网关联的站点。如果不存在这样的站点，则默认值为复制源域控制器的所在站点。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-ADDSReadOnlyDomainControllerAccount](./Add-ADDSReadOnlyDomainControllerAccount.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)
