---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamServer.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/update-ipamserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-IpamServer
---

# 更新 IpamServer

## 摘要
在操作系统升级后，更新相应的IPAM服务器配置。

## 语法

```
Update-IpamServer [-DeleteSystemCheckFailureRows] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Update-IpamServer` cmdlet 用于在操作系统升级后更新 IP 地址管理（IPAM）服务器。IPAM 的二进制文件和模式文件会随操作系统升级一起提供。如果没有任何可用的更新内容，将会发生错误。

作为IPAM服务器更新的一部分，此cmdlet执行以下步骤：

- Applies IPAM schema updates.
  The cmdlet performs data and schema validation of the existing IPAM database, and returns an error if the validation fails.
  A log is generated on the server in the %SystemDrive%\Windows\System32\IPAM\logs folder.
  If you specify the *DeleteSystemCheckFailureRows* parameter, the cmdlet proceeds to automatically delete the error rows.

- Completes any required data format transformation.
  This will not result in any loss of existing data.

- Applies changes in security groups and roles.

不会对任何现有的用户配置进行更改（例如将用户添加到安全组中），也不会修改IPAM任务调度的相关设置。如果出现错误，所有所做的更改都会被恢复到原始状态。

## 示例

### 示例 1：更新现有的 IPAM 安装
```
PS C:\> Update-IpamServer
Upgrading IPAM Server.

 As a part of upgrade, any changes in IPAM Server settings & configuration will be applied. Any requisite changes to database schema changes will be made. Do you want to continue?

[Y]Yes [N]No [S]Suspend [?]Help (default is "Y"): Y
```

此命令用于在操作系统升级后更新现有的 IPAM 安装。如果出现系统检查错误，该cmdlet将终止执行，并在 %System Drive%\System 32\IPAM\Logs 文件夹中生成一个日志文件。

### 示例 2：更新 IPAM 安装并删除系统检查失败的相关记录
```
PS C:\> Update-IpamServer -DeleteSystemCheckFailureRows
Upgrading IPAM Server.

 As a part of upgrade, any changes in IPAM Server settings & configuration will be applied. Any requisite changes to database schema changes will be made. Do you want to continue?

[Y]Yes [N]No [S]Suspend [?]Help (default is "Y"): Y
```

此命令用于在操作系统升级后更新现有的 IPAM（IP 地址管理）安装。即使遇到系统检查错误，该命令也不会终止执行，并会删除 IPAM 数据库中的冲突信息。命令会在 `%System Drive%\System 32\IPAM\Logs` 文件夹中生成日志文件。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
在运行该 cmdlet 之前会提示您进行确认。

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

### -DeleteSystemCheckFailureRows
表示该cmdlet在验证现有IPAM数据库的数据和架构时会自动删除错误行。如果系统检查失败，则会发生错误。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: DeleteErrorRows

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -ThrottleLimit
指定可以同时运行的并发操作的最大数量。如果省略了这个参数或输入了 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Windows PowerShell中的IP地址管理（IPAM）服务器cmdlet](./ipamserver.md)

