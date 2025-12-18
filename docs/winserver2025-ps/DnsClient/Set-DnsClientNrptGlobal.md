---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTGlobal_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/set-dnsclientnrptglobal?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsClientNrptGlobal
---

# Set-DnsClientNrptGlobal

## 摘要
修改全局名称解析策略表（NRPT）的设置。

## 语法

```
Set-DnsClientNrptGlobal [-EnableDAForAllNetworks <String>] [-GpoName <String>]
 [-SecureNameQueryFallback <String>] [-QueryPolicy <String>] [-Server <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsClientNrptGlobal` cmdlet 会修改以下全局名称解析策略表（NRPT）设置：

- DNS client enable Direct Access (DA) for all networks setting.
- DNS client query policy.
- DNS client secure name query fallback setting.

## 示例

### Example 1: Modify the NRPT settings
```
PS C:\> Set-DnsClientNrptGlobal -EnableDAForAllNetworks "disable" -PassThru

EnableDAForAllNetworks                  QueryPolicy                             SecureNameQueryFallback
----------------------                  -----------                             -----------------------
Disable                                 Disable                                 Disable
```

This command modifies the EnableDAForAllNetworks settings in the NPRT globally.

## 参数

### -AsJob
Runs the cmdlet as a background job. Use this parameter to run commands that take a long time to complete.

The cmdlet immediately returns an object that represents the job and then displays the command prompt.
You can continue to work in the session while the job completes.
To manage the job, use the `*-Job` cmdlets.
To get the job results, use the [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet.

For more information about Windows PowerShell background jobs, see [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251).

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

### -CimSession
Runs the cmdlet in a remote session or on a remote computer.
Enter a computer name or a session object, such as the output of a [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) or [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet.
The default is the current session on the local computer.

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

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

### -EnableDAForAllNetworks
Specifies DirectAccess (DA) settings.
The acceptable values for this parameter are:

- EnableOnNetworkID
- EnableAlways
- Disable
- DisableDA

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: EnableOnNetworkID, EnableAlways, Disable, DisableDA

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GpoName
Specifies the name of the Group Policy Object (GPO).
If this parameter is not specified, then the local NRPT settings are retrieved.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -QueryPolicy
Specifies the DNS client query policy.
The acceptable values for this parameter are:

- Disable
- QueryIPv6Only
- QueryBoth

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Disable, QueryIPv6Only, QueryBoth

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecureNameQueryFallback
Specifies the DNS client name resolution fallback policy.
The acceptable values for this parameter are:

- Disable
- FallbackSecure
- FallbackUnsecure
- FallbackPrivate

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Disable, FallbackSecure, FallbackUnsecure, FallbackPrivate

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
Specifies the server hosting the GPO.
This parameter is only applicable with the *GpoName* parameter.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳运行限制（即并发操作的最大数量）。这个限制仅适用于当前正在执行的命令，而不影响整个会话或整台计算机。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptGlobal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

`DnsClientNrptGlobal` 对象包含了 DNS 客户端 NRPT（Name Resolution Protocol Translation）全局设置的所有属性。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptGlobal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

`DnsClientNrptGlobal` 对象包含了 DNS 客户端 NRPT（Name Resolution Protocol Translation）全局设置的所有属性。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

